import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện
st.set_page_config(page_title="Gia Sư Tiếng Anh Lớp 5", page_icon="📚")
st.title("📚 Gia Sư Tiếng Anh Lớp 5")

# Lấy API Key từ Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Chưa tìm thấy API Key trong Secrets!")

# --- DÁN NỘI DUNG MARKDOWN VÀO ĐÂY ---
huong_dan_he_thong = """
[DÁN QUY TẮC VÀ KIẾN THỨC CỦA BẠN VÀO GIỮA HAI CỤM DẤU NHÁY KÉP NÀY]
"""

# Khởi tạo mô hình - ĐÃ CẬP NHẬT TÊN MÔ HÌNH CHUẨN
model = genai.GenerativeModel(
    model_name="gemini-3.1-flash-lite",
    system_instruction=huong_dan_he_thong
)

# Quản lý tin nhắn
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Con muốn hỏi gì nào?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Bắt đầu phiên chat với lịch sử
        chat = model.start_chat(history=[
            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} 
            for m in st.session_state.messages[:-1]
        ])
        response = chat.send_message(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Đã có lỗi xảy ra: {e}")
