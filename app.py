import streamlit as st
import google.generativeai as genai

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Gia Sư Tiếng Anh Lớp 5", page_icon="🌟", layout="centered")

# CSS để làm nút bấm đẹp hơn
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #008CBA;
        color: white;
        border-radius: 10px;
        width: 100%;
    }
    </style>
""", unsafe_allow_contents=True)

st.title("🌟 Gia Sư Tiếng Anh Lớp 5")
st.subheader("Chào mừng con đến với lớp học vui vẻ! ✨")

# --- KẾT NỐI AI ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Lỗi: Chưa có API Key!")

# NỘI DUNG MARKDOWN (Bạn giữ nguyên nội dung cũ của bạn nhé)
huong_dan_he_thong = """ [DÁN NỘI DUNG MARKDOWN CỦA BẠN VÀO ĐÂY] """

model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-lite",
    system_instruction=huong_dan_he_thong
)

# --- QUẢN LÝ TIN NHẮN ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# HIỆN LỜI CHÀO TỰ ĐỘNG NẾU CHƯA CHAT GÌ
if len(st.session_state.messages) == 0:
    welcome_text = "Chào con! Thầy/Cô rất vui được gặp con. Hôm nay con muốn cùng Thầy/Cô làm gì nào? Con có thể chọn các nút bên dưới hoặc tự gõ câu hỏi nhé! 👇"
    st.session_state.messages.append({"role": "assistant", "content": welcome_text})

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CÁC NÚT BẤM GỢI Ý CHO BÉ ---
st.write("---")
st.write("**Con muốn Thầy/Cô giúp gì nào?**")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 Ôn tập Unit 11"):
        st.session_state.clicked_prompt = "Thầy ơi, giúp con ôn tập từ vựng và ngữ pháp của Unit 11 nhé!"
with col2:
    if st.button("🏆 Làm đề thi HK2"):
        st.session_state.clicked_prompt = "Cô ơi, ra đề thi thử Học kỳ 2 cho con làm nhé!"
with col3:
    if st.button("🎮 Giải đố từ vựng"):
        st.session_state.clicked_prompt = "Mình chơi trò chơi giải đố từ vựng đi Thầy!"

# --- XỬ LÝ LỆNH TỪ NÚT BẤM HOẶC Ô CHAT ---
prompt = st.chat_input("Gõ câu trả lời hoặc câu hỏi của con...")

# Ưu tiên lấy lệnh từ nút bấm nếu có
if "clicked_prompt" in st.session_state:
    prompt = st.session_state.clicked_prompt
    del st.session_state.clicked_prompt

if prompt:
    # Lưu và hiển thị câu hỏi
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI trả lời
    try:
        chat = model.start_chat(history=[
            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} 
            for m in st.session_state.messages[:-1]
        ])
        with st.chat_message("assistant"):
            response = chat.send_message(prompt)
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Lỗi rồi: {e}")
