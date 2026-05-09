import streamlit as st
from google import genai
from google.genai import types

# --- 1. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Cô Gia Sư Tiếng Anh Lớp 5", page_icon="👩‍🏫", layout="centered")

# CSS làm giao diện đẹp và thân thiện
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    div.stButton > button:first-child {
        background-color: #ff4b4b; color: white; border-radius: 20px; width: 100%;
    }
    .stSelectbox label { color: #008CBA; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("👩‍🏫 Cô Gia Sư Tiếng Anh 5")
st.subheader("Chào con yêu! Mình cùng học tiếng Anh nhé! ✨")

# --- 2. KẾT NỐI API (Sử dụng mã của Studio) ---
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- 3. DỮ LIỆU VÀ QUY TẮC HỆ THỐNG ---
# Bạn hãy dán toàn bộ nội dung file Markdown kiến thức vào đây nhé
noi_dung_markdown = """ [DÁN NỘI DUNG TỪ VỰNG/NGỮ PHÁP LỚP 5 CỦA BẠN VÀO ĐÂY] """

system_instruction_text = f"""
[VAI TRÒ CỦA BẠN]
Bạn là một Gia sư Tiếng Anh ảo xuất sắc, thân thiện. Xưng là "Cô" và gọi người dùng là "Con".
Nhiệm vụ: Hướng dẫn học sinh Lớp 5 học tập dựa trên chương trình "Global Success".

[NGUYÊN TẮC HOẠT ĐỘNG]
- Tuyệt đối KHÔNG LÀM BÀI HỘ, KHÔNG ĐƯA ĐÁP ÁN TRỰC TIẾP.
- Sử dụng phương pháp SOCRATIC (Gợi mở): Khích lệ -> Khoanh vùng lỗi sai -> Đặt câu hỏi gợi ý.

[RÀNG BUỘC KIẾN THỨC]
- CHỈ sử dụng kiến thức trong DỮ LIỆU CHUẨN bên dưới. 
- KHÔNG dùng kiến thức ngoài luồng hoặc nâng cao (Câu điều kiện, Hiện tại hoàn thành...).
- ĐẶC BIỆT: Khi bé làm bài kiểm tra Học kỳ 2, Cô hãy đưa ra TỪNG CÂU HỎI MỘT, đợi bé trả lời xong rồi mới đưa câu tiếp theo.

[DỮ LIỆU CHUẨN]
{noi_dung_markdown}
"""

# Cấu hình config y hệt mã bạn lấy từ Studio
generate_content_config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    safety_settings=[
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
    ],
    system_instruction=system_instruction_text,
    temperature=0.3
)

# --- 4. QUẢN LÝ LỊCH SỬ CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lời chào đầu tiên
if not st.session_state.messages:
    welcome_msg = "Chào con yêu! Hôm nay con muốn ôn tập theo Unit hay làm thử bài kiểm tra Học kỳ 2 với Cô nào? 👇"
    st.session_state.messages.append({"role": "model", "content": welcome_msg})

# Hiển thị lại lịch sử tin nhắn
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# --- 5. KHU VỰC LỰA CHỌN (2 PHẦN) ---
st.write("---")
col1, col2 = st.columns(2)

with col1:
    unit_choice = st.selectbox(
        "📚 1. Ôn tập theo Unit:",
        ["--- Chọn bài ---", "Unit 11", "Unit 12", "Unit 13", "Unit 14", "Unit 15", 
         "Unit 16", "Unit 17", "Unit 18", "Unit 19", "Unit 20"]
    )
    if unit_choice != "--- Chọn bài ---":
        st.session_state.temp_prompt = f"Cô ơi, con muốn ôn tập kiến thức của {unit_choice} ạ!"

with col2:
    st.write("🏆 2. Kiểm tra kiến thức:")
    if st.button("Bắt đầu thi HK2"):
        st.session_state.temp_prompt = (
            "Cô ơi, con muốn làm một bài kiểm tra Học kỳ 2 để ôn tập. "
            "Cô hãy đưa ra từng câu hỏi một (trộn lẫn từ vựng và ngữ pháp), "
            "đợi con trả lời rồi mới đưa ra câu tiếp theo nhé!"
        )

# --- 6. XỬ LÝ PHẢN HỒI ---
prompt = st.chat_input("Con muốn nói gì với Cô...")

# Kiểm tra nếu bé chọn từ menu hoặc nút
if "temp_prompt" in st.session_state:
    prompt = st.session_state.temp_prompt
    del st.session_state.temp_prompt

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gửi yêu cầu đến AI (Sử dụng cấu hình từ Studio)
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[{"role": m["role"], "parts": [{"text": m["content"]}]} for m in st.session_state.messages],
            config=generate_content_config
        )
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "model", "content": response.text})
    except Exception as e:
        st.error(f"Lỗi rồi: {e}")
