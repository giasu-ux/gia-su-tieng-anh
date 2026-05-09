import streamlit as st
from google import genai
from google.genai import types

# --- CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="Cô Gia Sư Tiếng Anh Lớp 5", page_icon="👩‍🏫")
st.title("👩‍🏫 Cô Gia Sư Tiếng Anh 5")

# --- KẾT NỐI API ---
# Lấy API Key từ Secrets của Streamlit
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- CHUẨN BỊ NỘI DUNG HỆ THỐNG ---
# Ở đây, bạn dán thêm toàn bộ nội dung file Markdown kiến thức vào sau phần vai trò
noi_dung_markdown = """ [DÁN NỘI DUNG TỪ VỰNG/NGỮ PHÁP CỦA BẠN VÀO ĐÂY] """

# Cấu hình giống hệt mã bạn lấy từ Studio
generate_content_config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"), # Theo mã bạn gửi
    safety_settings=[
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
    ], # Theo mã bạn gửi
    system_instruction= f"""[VAI TRÒ CỦA BẠN]
Bạn là một Gia sư Tiếng Anh ảo xuất sắc... (Dán toàn bộ phần hướng dẫn của bạn ở đây)

[DỮ LIỆU CHUẨN]
{noi_dung_markdown}""" # Theo mã bạn gửi
)

# --- QUẢN LÝ LỊCH SỬ CHAT ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Hiển thị tin nhắn cũ
for message in st.session_state.chat_history:
    with st.chat_message("user" if message['role'] == "user" else "assistant"):
        st.markdown(message['content'])

# --- XỬ LÝ NHẬP LIỆU ---
if prompt := st.chat_input("Con muốn hỏi Cô gì nào?"):
    # Hiển thị tin nhắn của bé
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Gửi lệnh cho AI (Sử dụng cấu hình từ Studio)
    # Chúng ta gửi toàn bộ lịch sử để AI không quên "Cô - Con"
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite", # Theo mã bạn gửi
        contents=[{"role": "user", "parts": [{"text": m["content"]}]} for m in st.session_state.chat_history] + 
                 [{"role": "user", "parts": [{"text": prompt}]}],
        config=generate_content_config
    )

    # Hiển thị phản hồi của Cô
    with st.chat_message("assistant"):
        st.markdown(response.text)
    
    # Lưu vào lịch sử
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
