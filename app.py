import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện
st.set_page_config(page_title="Gia Sư Tiếng Anh Lớp 5", page_icon="📚")
st.title("📚 Gia Sư Tiếng Anh Lớp 5")

# Lấy API Key từ Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Chưa tìm thấy API Key! Bạn nhớ gài vào phần Advanced Settings > Secrets nhé.")

# --- PHẦN NÀY DÁN NỘI DUNG ---
# Lưu ý: Giữ nguyên 3 dấu nháy kép ở đầu và cuối
noi_dung_huong_dan = """
[BẠN DÁN TOÀN BỘ QUY TẮC VÀ KIẾN THỨC MÀU XANH TRONG FILE MARKDOWN VÀO ĐÂY]
"""

# Khởi tạo model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=noi_dung_huong_dan
)

# Xử lý chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Con muốn hỏi gì nào?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = model.start_chat(history=[
            {"role": m["role"], "parts": [m["content"]]} 
            for m in st.session_state.messages[:-1]
        ])
        response = chat.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
