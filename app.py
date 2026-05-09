import streamlit as st
from google import genai
from google.genai import types

# --- 1. CẤU HÌNH GIAO DIỆN (UI) ---
st.set_page_config(page_title="Cô Gia Sư Tiếng Anh 5", page_icon="👩‍🏫", layout="wide")

# CSS làm đẹp giao diện: Sidebar màu xanh dịu, khung chat bo tròn thân thiện
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

# --- 2. KẾT NỐI API GOOGLE AI (Sử dụng mã của Studio) ---
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# --- 3. KHO DỮ LIỆU KIẾN THỨC GLOBAL SUCCESS 5 ---
# Toàn bộ nội dung con cung cấp đã được đưa vào đây
noi_dung_nguon = """
# TỪ VỰNG - NGỮ PHÁP TIẾNG ANH 5 GLOBAL SUCCESS

## CLASSROOM LANGUAGES (Ngôn ngữ lớp học)
- Stand up, Sit down, Come in, May I come in, Don't talk, May I ask a question, May I go out, Open/Close your book, Sorry I'm late...

## UNIT 1: ALL ABOUT ME
- Từ vựng: yourself, baseball, basketball, beautifully, countryside, dolphin, panda, sandwich, subject...
- Ngữ pháp: Tell me about yourself (My name is..., I'm in Class..., I live in...); Favourite (What's your favourite colour? It's blue).

## UNIT 2: OUR HOMES
- Từ vựng: address, grade, building, district, flat, tower...
- Ngữ pháp: What's your address? (It's 50 Hoa Binh Street); Where do you live? (I live at...).

## UNIT 3: MY FOREIGN FRIENDS
- Từ vựng: foreign, nationality, Australia/Australian, Japan/Japanese, friendly, helpful, active, clever...
- Ngữ pháp: Where are you from? What nationality is she? What's he like? (He's friendly).

## UNIT 4: OUR FREE TIME ACTIVITIES
- Từ vựng: go for a walk, play the violin, surf the internet, water the flowers. Trạng từ: always, usually, often, sometimes, rarely, never.
- Ngữ pháp: What do you like in your free time? What does he do at the weekend?

## UNIT 5: MY FUTURE JOB
- Từ vựng: firefighter, reporter, gardener, teach children, report the news, take care of.
- Ngữ pháp: What would you like to be in the future? (I'd like to be a doctor). Why? (Because I'd like to help people).

## UNIT 6 - UNIT 20: TỔNG HỢP KIẾN THỨC
- Unit 6: Vị trí phòng học (Ground floor, first floor), Chỉ đường (Turn left/right).
- Unit 11: Family time (Quá khứ đơn: went, ate, saw, bought, swam).
- Unit 14: Stay healthy (How often do you...? Tần suất).
- Unit 15: Health (What's the matter? I have a headache. You should/shouldn't...).
- Unit 16: Seasons (How's the weather? What do you wear?).
- Unit 17: Stories (Who are the main characters?).
- Unit 18-19: Travel & Places (Where do you want to visit? How can I get there?).

## PHỤ LỤC NGỮ PHÁP
- Thì Hiện tại đơn (Simple Present), Trạng từ chỉ tần suất (Always, usually...).
- Thì Quá khứ đơn (Past Simple): Quy tắc thêm -ed và Động từ bất quy tắc thông dụng.
"""

# --- 4. CHỈ DẪN HỆ THỐNG (SYSTEM INSTRUCTION) ---
system_instruction_text = f"""
[VAI TRÒ]
Bạn là một Gia sư Tiếng Anh ảo xuất sắc, thân thiện, kiên nhẫn và tận tâm. Nhiệm vụ duy nhất của bạn là đồng hành, hướng dẫn học sinh Lớp 5 (10-11 tuổi) học tập dựa trên chương trình sách giáo khoa "Global Success".

[NGUYÊN TẮC HOẠT ĐỘNG TỐI THƯỢNG]
- Tuyệt đối KHÔNG LÀM BÀI HỘ, KHÔNG ĐƯA ĐÁP ÁN TRỰC TIẾP ngay từ lần hỏi đầu tiên. Bạn phải đóng vai trò là người dẫn dắt, giúp học sinh tự tư duy và tìm ra câu trả lời.
- Chỉ sử dụng kiến thức trong [DỮ LIỆU CHUẨN]. KHÔNG dạy kiến thức nâng cao lớp trên.

[PHƯƠNG PHÁP SƯ PHẠM: SOCRATIC METHOD (GỢI MỞ)]
Khi học sinh làm bài tập, đặt câu hỏi hoặc làm sai, hãy áp dụng nghiêm ngặt quy trình 3 bước sau:
1. Khích lệ: Bắt đầu bằng thái độ tích cực (VD: "Câu này con có ý tưởng rất hay!").
2. Khoanh vùng lỗi sai: Chỉ ra từ hoặc cụm từ chưa chính xác một cách nhẹ nhàng.
3. Đặt câu hỏi gợi ý: Sử dụng kiến thức trong dữ liệu chuẩn để đặt câu hỏi giúp học sinh nhớ lại quy tắc.

[CHẾ ĐỘ KIỂM TRA & TRÒ CHƠI]
- Bài thi HK2: Đưa ra TỪNG CÂU HỎI MỘT, đợi con trả lời xong mới nhận xét và đưa câu tiếp theo.
- Trò chơi Sắp xếp từ: Lấy 1 từ trong dữ liệu, xáo trộn chữ cái (VD: l-h-o-p-d-n-i) và đố con. TUYỆT ĐỐI KHÔNG được nhắc đến từ gốc hay viết từ gốc ra màn hình trước khi con đoán đúng.
- Simon Says: Dùng Classroom Languages để ra lệnh cho con.

[XƯNG HÔ & GIỌNG ĐIỆU]
- Xưng là "Cô" và gọi người dùng là "Con". Giọng điệu vui tươi, thỉnh thoảng dùng emoji 🌟, 😊, 📚.

[DỮ LIỆU CHUẨN]
{noi_dung_nguon}
"""

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="MINIMAL"),
    system_instruction=system_instruction_text,
    temperature=0.2, # Giúp cô tập trung, bớt nói leo kiến thức ngoài
    safety_settings=[
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_LOW_AND_ABOVE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_LOW_AND_ABOVE"),
    ]
)

# --- 5. QUẢN LÝ LỊCH SỬ CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 6. THANH ĐIỀU KHIỂN BÊN TRÁI (SIDEBAR) ---
with st.sidebar:
    st.title("🎮 Trung tâm học tập")
    
    # PHẦN 1: ÔN TẬP UNIT
    unit_choice = st.selectbox(
        "📚 Chọn bài ôn tập:",
        ["--- Chọn bài ---"] + [f"Unit {i}" for i in range(1, 21)]
    )
    if unit_choice != "--- Chọn bài ---":
        st.session_state.nav_prompt = f"Cô ơi, con muốn ôn tập kiến thức của {unit_choice} ạ!"

    st.write("---")
    
    # PHẦN 2: LUYỆN ĐỀ & TRÒ CHƠI
    st.write("🏆 Thử thách vui vẻ:")
    
    if st.button("🚀 Bắt đầu thi HK2"):
        st.session_state.nav_prompt = "Cô ơi, ra bài thi HK2 từng câu một cho con làm nhé!"
        
    if st.button("🧩 Game: Sắp xếp từ"):
        st.session_state.nav_prompt = "Cô ơi, mình chơi trò sắp xếp chữ cái từ vựng đi ạ!"
        
    if st.button("🧙‍♂️ Đố vui Ngữ pháp"):
        st.session_state.nav_prompt = "Cô đố con về các động từ quá khứ bất quy tắc đi ạ!"

    st.write("---")
    if st.button("🗑️ Xóa hội thoại cũ"):
        st.session_state.messages = []
        st.rerun()

# --- 7. KHU VỰC TRÒ CHUYỆN CHÍNH ---
st.title("👩‍🏫 Cô Gia Sư Tiếng Anh 5")

# Lời chào nếu chưa có tin nhắn
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("Chào con yêu! Cô đã sẵn sàng đồng hành cùng con rồi. Con hãy chọn một hoạt động thú vị ở thanh bên trái để mình bắt đầu nhé! ✨")

# Hiển thị lịch sử chat
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# --- 8. XỬ LÝ PHẢN HỒI ---
prompt = st.chat_input("Con muốn nói gì với Cô...")

# Kiểm tra nếu con bấm nút ở Sidebar
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
