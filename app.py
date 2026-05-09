import streamlit as st
from google import genai
from google.genai import types

# --- 1. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Cô Gia Sư Tiếng Anh 5", page_icon="👩‍🏫", layout="wide")

# CSS làm đẹp giao diện, làm khung chat mềm mại và Sidebar chuyên nghiệp
st.markdown("""
    <style>
    .stApp { background-color: #f8faff; }
    [data-testid="stSidebar"] { background-color: #e3f2fd; border-right: 2px solid #008CBA; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    div.stButton > button:first-child {
        background-color: #ff4b4b; color: white; border-radius: 20px; width: 100%; font-weight: bold;
    }
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 2. KẾT NỐI API ---
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- 3. DỮ LIỆU VÀ CHỈ DẪN HỆ THỐNG ---
# (Phần này con dán lại nội dung Markdown kiến thức Global Success như cũ nhé)
noi_dung_markdown = """ # TỪ VỰNG - NGỮ PHÁP TIẾNG ANH 5 GLOBAL SUCCESS [cite: 1]
- Bao gồm Classroom Languages [cite: 2], Unit 1-20 [cite: 45, 74, 107, 138] và Phụ lục Ngữ pháp.
- Chi tiết Class Languages: Stand up [cite: 3], Sit down [cite: 4], Open your book[cite: 11]...
- Chi tiết Unit 11: Past Simple với Động từ bất quy tắc (buy-bought, do-did, go-went...).
- Chi tiết Ngữ pháp: Hiện tại đơn, Quá khứ đơn, Trạng từ chỉ tần suất.
 """

system_instruction_text = f"""
[VAI TRÒ] Cô Gia sư Tiếng Anh (Xưng Cô - gọi Con).
[NGUYÊN TẮC] Socratic Method (Gợi mở), không đưa đáp án ngay.
[KIẾN THỨC] CHỈ dùng Global Success Lớp 5. KHÔNG dùng kiến thức nâng cao.
[BÀI THI] Hỏi từng câu một, đợi con trả lời mới đưa câu tiếp theo.
[DỮ LIỆU] {noi_dung_markdown}
"""

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    system_instruction=system_instruction_text,
    temperature=0.3
)

# --- 4. QUẢN LÝ LỊCH SỬ CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 5. THANH ĐIỀU KHIỂN BÊN TRÁI (SIDEBAR) ---
with st.sidebar:
    st.title("🎮 Trung tâm học tập")
    st.write("Con chọn bài học ở đây nhé!")
    
    # 1. Chọn Unit
    unit_choice = st.selectbox(
        "📚 Ôn tập theo Unit:",
        ["--- Chọn bài ---", "Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", 
         "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10", "Unit 11", "Unit 12",
         "Unit 13", "Unit 14", "Unit 15", "Unit 16", "Unit 17", "Unit 18", "Unit 19", "Unit 20"]
    )
    if unit_choice != "--- Chọn bài ---":
        st.session_state.nav_prompt = f"Cô ơi, con muốn ôn tập kiến thức của {unit_choice} ạ!"

    st.write("---")
    
    # 2. Nút làm đề thi
    st.write("🏆 Kiểm tra kiến thức:")
    if st.button("🚀 Bắt đầu thi HK2"):
        st.session_state.nav_prompt = (
            "Cô ơi, con muốn làm một bài kiểm tra Học kỳ 2 để ôn tập. "
            "Cô hãy đưa ra từng câu hỏi một (trộn cả từ vựng và ngữ pháp), "
            "đợi con trả lời xong mới đưa câu tiếp theo nhé!"
        )
    
    st.write("---")
    if st.button("🗑️ Xóa lịch sử chat"):
        st.session_state.messages = []
        st.rerun()

# --- 6. KHU VỰC TRÒ CHUYỆN CHÍNH (MAIN AREA) ---
st.title("👩‍🏫 Cô Gia Sư Tiếng Anh 5")

# Lời chào đầu tiên nếu chưa có tin nhắn
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("Chào con yêu! Cô đã sẵn sàng rồi. Con hãy chọn bài học ở bên trái hoặc gõ câu hỏi cho Cô nhé! ✨")

# Hiển thị lịch sử chat sạch sẽ
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# --- 7. XỬ LÝ PHẢN HỒI ---
prompt = st.chat_input("Con gõ câu trả lời hoặc thắc mắc vào đây...")

# Kiểm tra lệnh từ Sidebar
if "nav_prompt" in st.session_state:
    prompt = st.session_state.nav_prompt
    del st.session_state.nav_prompt

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[{"role": m["role"], "parts": [{"text": m["content"]}]} for m in st.session_state.messages],
            config=config
        )
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "model", "content": response.text})
    except Exception as e:
        st.error(f"Lỗi: {e}")
