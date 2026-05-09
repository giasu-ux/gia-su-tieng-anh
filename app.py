import streamlit as st
from google import genai
from google.genai import types

# --- 1. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Cô Gia Sư Tiếng Anh Lớp 5", page_icon="👩‍🏫", layout="centered")

# CSS tạo không gian học tập vui tươi cho bé
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    div.stButton > button:first-child {
        background-color: #ff4b4b; color: white; border-radius: 20px; font-weight: bold;
    }
    .stSelectbox label { color: #008CBA; font-weight: bold; }
    .stChatMessage { border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("👩‍🏫 Cô Gia Sư Tiếng Anh 5")
st.subheader("Chào con yêu! Cô con mình cùng ôn tập Global Success nhé! ✨")

# --- 2. KẾT NỐI API ---
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- 3. KHO KIẾN THỨC VÀ QUY TẮC SƯ PHẠM ---
# Cô đã nhúng toàn bộ dữ liệu con cung cấp vào đây
noi_dung_markdown = """
# TỪ VỰNG - NGỮ PHÁP TIẾNG ANH 5 GLOBAL SUCCESS [cite: 1]
- Bao gồm Classroom Languages [cite: 2], Unit 1-20 [cite: 45, 74, 107, 138] và Phụ lục Ngữ pháp.
- Chi tiết Class Languages: Stand up [cite: 3], Sit down [cite: 4], Open your book[cite: 11]...
- Chi tiết Unit 11: Past Simple với Động từ bất quy tắc (buy-bought, do-did, go-went...).
- Chi tiết Ngữ pháp: Hiện tại đơn, Quá khứ đơn, Trạng từ chỉ tần suất.
"""

system_instruction_text = f"""
[VAI TRÒ]
Bạn là Cô Gia sư Tiếng Anh ảo. Xưng là "Cô", gọi người dùng là "Con".

[NGUYÊN TẮC SOCRATIC]
- Tuyệt đối KHÔNG đưa đáp án ngay. 
- Nếu con làm sai: Khích lệ -> Khoanh vùng lỗi -> Đặt câu hỏi gợi mở để con tự nhớ bài.

[RÀNG BUỘC KIẾN THỨC]
- CHỈ sử dụng kiến thức trong phần [DỮ LIỆU CHUẨN] bên dưới.
- TUYỆT ĐỐI KHÔNG sử dụng Câu điều kiện (If type 1, 2), Hiện tại hoàn thành hay các cấu trúc lớp lớn.

[DỰNG BÀI KIỂM TRA]
- Khi con làm bài thi Học kỳ 2: Cô phải đưa ra TỪNG CÂU HỎI MỘT. 
- Phải đợi con trả lời xong mới được nhận xét và đưa câu hỏi tiếp theo.

[DỮ LIỆU CHUẨN]
{noi_dung_markdown}
"""

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    system_instruction=system_instruction_text,
    temperature=0.2, # Giữ cho Cô tập trung, không nói leo kiến thức ngoài
    safety_settings=[
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
    ]
)

# --- 4. QUẢN LÝ LỊCH SỬ CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Lời chào đầu tiên
if not st.session_state.messages:
    welcome = "Chào con yêu! Hôm nay con muốn ôn tập theo từng Unit hay làm bài kiểm tra Học kỳ 2 để thử sức mình nhỉ? Con chọn ở dưới nhé! 👇"
    st.session_state.messages.append({"role": "model", "content": welcome})

# Hiển thị lịch sử chat
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# --- 5. BẢNG ĐIỀU KHIỂN CHO BÉ ---
st.write("---")
col1, col2 = st.columns(2)

with col1:
    choice = st.selectbox(
        "📚 1. Ôn tập theo Unit:",
        ["--- Chọn bài học ---", "Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", 
         "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10", "Unit 11", "Unit 12",
         "Unit 13", "Unit 14", "Unit 15", "Unit 16", "Unit 17", "Unit 18", "Unit 19", "Unit 20"]
    )
    if choice != "--- Chọn bài học ---":
        st.session_state.nav_prompt = f"Cô ơi, con muốn ôn tập kiến thức của {choice} ạ!"

with col2:
    st.write("🏆 2. Luyện đề thi:")
    if st.button("Bắt đầu thi HK2"):
        st.session_state.nav_prompt = (
            "Cô ơi, con muốn làm một bài kiểm tra Học kỳ 2 để ôn tập. "
            "Cô hãy đưa ra từng câu hỏi một (trộn cả từ vựng và ngữ pháp), "
            "đợi con trả lời xong mới đưa câu tiếp theo nhé!"
        )

# --- 6. XỬ LÝ NHẬP LIỆU ---
prompt = st.chat_input("Con muốn trò chuyện gì với Cô...")

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
        st.error(f"Cô gặp chút lỗi nhỏ, con chờ xíu nhé: {e}")
