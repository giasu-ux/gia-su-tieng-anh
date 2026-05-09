import streamlit as st
import google.generativeai as genai

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Cô Gia Sư Tiếng Anh Lớp 5", page_icon="👩‍🏫", layout="centered")

# CSS làm giao diện thân thiện với trẻ em
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    div.stButton > button:first-child {
        background-color: #ff4b4b; color: white; border-radius: 20px;
    }
    .stSelectbox label { color: #008CBA; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("👩‍🏫 Cô Gia Sư Tiếng Anh 5")
st.subheader("Chào con yêu! Hôm nay mình cùng học thật vui nhé! ✨")

# --- KẾT NỐI AI ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Lỗi: Cô chưa tìm thấy API Key trong mục Secrets!")

# NỘI DUNG MARKDOWN (Nhớ dán toàn bộ dữ liệu Global Success của bạn vào đây)
huong_dan_he_thong = """ [DÁN NỘI DUNG MARKDOWN CỦA BẠN VÀO ĐÂY] """

model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-lite",
    system_instruction=huong_dan_he_thong
)

# --- QUẢN LÝ TIN NHẮN ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Lời chào đầu tiên từ Cô
if len(st.session_state.messages) == 0:
    welcome = "Chào con! Cô rất vui được đồng hành cùng con. Con muốn Cô hướng dẫn ôn tập Unit nào hay muốn thử sức làm đề thi học kỳ 2 nhỉ? Con chọn ở dưới nhé! 👇"
    st.session_state.messages.append({"role": "assistant", "content": welcome})

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- KHU VỰC ĐIỀU KHIỂN TỰ CHỌN (DROPDOWN) ---
st.write("---")
col1, col2 = st.columns([2, 1])

with col1:
    # Cho bé tự chọn Unit muốn học
    unit_choice = st.selectbox(
        "📚 Con muốn ôn tập bài nào?",
        ["--- Chọn Unit ---", "Unit 11", "Unit 12", "Unit 13", "Unit 14", "Unit 15", 
         "Unit 16", "Unit 17", "Unit 18", "Unit 19", "Unit 20"]
    )
    if unit_choice != "--- Chọn Unit ---":
        st.session_state.clicked_prompt = f"Cô ơi, giúp con ôn tập kiến thức của {unit_choice} nhé!"

with col2:
    # Nút làm đề thi vẫn giữ để bé luyện tập
    if st.button("🏆 Làm đề HK2"):
        st.session_state.clicked_prompt = "Cô ơi, ra đề thi thử Học kỳ 2 cho con làm nhé!"

# --- XỬ LÝ PHẢN HỒI ---
prompt = st.chat_input("Con gõ câu hỏi hoặc câu trả lời ở đây...")

if "clicked_prompt" in st.session_state:
    prompt = st.session_state.clicked_prompt
    del st.session_state.clicked_prompt

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

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
        st.error(f"Có lỗi nhỏ rồi, con chờ chút nhé: {e}")
