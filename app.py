import streamlit as st
from google import genai
from google.genai import types

# --- 1. CẤU HÌNH GIAO DIỆN NÂNG CAO ---
st.set_page_config(page_title="English For Kids!", page_icon="🐱", layout="wide")

# CSS để giả lập giao diện chuyên nghiệp như ảnh thiết kế
st.markdown("""
    <style>
    /* Tổng thể ứng dụng */
    .stApp {
        background-color: #F8FAFF;
    }
    
    /* Thanh bên trái (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #EBF4FF;
        border-right: 1px solid #D1E9FF;
    }
    
    /* Mascot và Logo ở Sidebar */
    .sidebar-header {
        text-align: center;
        padding: 20px 0;
    }

   /* Khung chứa tổng thể */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 35px; /* Tăng khoảng cách trên dưới lên 35px cho thoáng hẳn */
        padding: 20px 0px;
        width: 100%;
    }

    .chat-row {
        display: flex;
        width: 100%;
        align-items: flex-end;
    }

    /* Con (Người học) - Bây giờ ở bên PHẢI */
    .user-row { 
        justify-content: flex-end; 
    }
    
    /* Cô (Gia sư) - Bây giờ ở bên TRÁI */
    .ai-row { 
        justify-content: flex-start; 
    }

    .chat-bubble {
        padding: 12px 18px;
        border-radius: 20px;
        max-width: 75%;
        font-size: 16px;
        line-height: 1.5;
        box-shadow: 2px 4px 15px rgba(0,0,0,0.1) !important;
    }

    /* Bong bóng của Con: Màu Tím Gradient */
    .user-bubble {
        background: linear-gradient(90deg, #A78BFA 0%, #8B5CF6 100%) !important;
        color: white !important;
        margin-right: 10px;
        border-bottom-right-radius: 2px;
    }

    /* Bong bóng của Cô: Màu Trắng */
    .ai-bubble {
        background-color: white !important;
        color: #333 !important;
        margin-left: 10px;
        border-bottom-left-radius: 2px;
    }

    .chat-icon {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Banner màu tím phía trên */
    .top-banner {
        background: linear-gradient(90deg, #A78BFA 0%, #8B5CF6 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    /* Tùy chỉnh nút bấm */
    div.stButton > button {
        border-radius: 12px;
        height: 3em;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    /* Nút "Bắt đầu thi HK2" màu tím */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #A78BFA 0%, #8B5CF6 100%);
        color: white;
        border: none;
        border-radius: 12px;
        height: 3em;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1)
    }

    .nut-xoa-hoi-thoai {
    /* Dải màu đỏ pastel dịu nhẹ */
    background: linear-gradient(135deg, #ffcfcf 0%, #ff9a9a 100%) !important;
    
    /* Các thuộc tính bổ trợ để nút trông đẹp hơn */
    border: none !important;
    color: white !important;
    padding: 10px 20px;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s;
    
    /* Đổ bóng nhẹ để nút có chiều sâu (tránh bị phẳng lì) */
    box-shadow: 0 4px 15px rgba(255, 154, 154, 0.3) !important;

}

/* Hiệu ứng khi di chuột qua */
.nut-xoa-hoi-thoai:hover {
    opacity: 0.9;
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(255, 154, 154, 0.4);
}

    /* Khung nhập liệu ở dưới */
    [data-testid="stChatInput"] {
        border-radius: 30px;
        border: 2px solid #E0E7FF;
    }
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

[CẤU TRÚC ĐỀ THI HK2 & TRÒ CHƠI]
Khi con nhấn "Bắt đầu thi HK2", Cô phải đưa ra TỪNG CÂU HỎI MỘT, đợi con trả lời xong mới nhận xét và đưa câu tiếp theo. Cô hãy luân phiên sử dụng 6 dạng bài sau:
- Dạng 1 (Định nghĩa): Đưa mô tả tiếng Anh, con chọn từ đúng (VD: Season with hot weather -> Summer).
- Dạng 2 (Trắc nghiệm): Câu văn có lựa chọn trong ngoặc hoặc A/B/C.
- Dạng 3 (Đọc hiểu): Đưa đoạn văn ngắn và hỏi True/False hoặc trắc nghiệm.
- Dạng 4 (Sắp xếp câu): Đưa các từ xáo trộn để con viết lại thành câu đúng.
- Dạng 5 (Điền từ): Đưa đoạn văn có ô trống (1), (2) và danh sách từ gợi ý.
- Dạng 6 (Trả lời theo gợi ý): Hỏi và cho từ gợi ý trong ngoặc.

[LUẬT CHƠI GAME SẮP XẾP TỪ - QUAN TRỌNG]
- Cô chọn 1 từ trong [DỮ LIỆU CHUẨN].
- Cô CHỈ ĐƯỢC đưa ra dãy chữ cái đã xáo trộn. 
- TUYỆT ĐỐI KHÔNG được nhắc đến từ gốc hay viết từ gốc ra màn hình trước khi con đoán. 
- Ví dụ sai: "'apple' xáo trộn thành 'plepa'" -> BỊ CẤM.
- Ví dụ đúng: "Cô có dãy chữ này: 'p-l-e-p-a'. Con đoán xem đây là quả gì nào?"

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
def call_ai_now(user_input):
    # 1. Thêm tin nhắn của con vào bộ nhớ
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 2. Hiển thị ngay lập tức tin nhắn của con lên màn hình
    with st.chat_message("user", avatar="👦"):
        st.markdown(user_input)

    # 3. Tạo hiệu ứng "Cô đang suy nghĩ..."
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Cô đang suy nghĩ câu trả lời cho con nhé..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=[{"role": "user" if m["role"] == "user" else "model", "parts": [{"text": m["content"]}]} for m in st.session_state.messages],
                    config=config
                )
                ai_text = response.text
                st.markdown(ai_text)
                # Lưu câu trả lời của Cô vào bộ nhớ
                st.session_state.messages.append({"role": "model", "content": ai_text})
            except Exception as e:
                st.error(f"Cô gặp chút lỗi nhỏ: {e}")

def on_sidebar_action():
    # (Giữ nguyên hàm này để xử lý nút chọn Unit)
    if st.session_state.unit_selector != "--- Chọn bài ---":
        unit = st.session_state.unit_selector
        call_ai_now(f"Cô ơi, con muốn ôn tập kiến thức của {unit} ạ!")
        st.session_state.unit_selector = "--- Chọn bài ---"
        
def display_message(role, content):
    if role == "user":
        # === ICON BÉ TRAI DỄ THƯƠNG (Thay đổi tại đây) ===
        user_icon_url = "https://cdn-icons-png.flaticon.com/512/9136/9136536.png" 
        
        # Con (User) bên PHẢI: [Tin nhắn] [Icon]
        st.markdown(f"""
            <div class="chat-row user-row">
                <div class="chat-bubble user-bubble">{content}</div>
                <img src="{user_icon_url}" class="chat-icon">
            </div>
        """, unsafe_allow_html=True)
    else:
        # === ICON CÔ GIÁO HIỀN DỊU (Thay đổi tại đây) ===
        teacher_icon_url = "https://cdn-icons-png.flaticon.com/512/7439/7439481.png"
        
        # Cô (Model) bên TRÁI: [Icon] [Tin nhắn]
        st.markdown(f"""
            <div class="chat-row ai-row">
                <img src="{teacher_icon_url}" class="chat-icon">
                <div class="chat-bubble ai-bubble">{content}</div>
            </div>
        """, unsafe_allow_html=True)
        
# --- 5. QUẢN LÝ LỊCH SỬ CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 6. HÀM XỬ LÝ KHI CHỌN UNIT (Sửa lỗi kẹt Unit) ---
def handle_unit_change():
    if st.session_state.unit_selector != "--- Chọn bài ---":
        st.session_state.nav_prompt = f"Cô ơi, con muốn ôn tập kiến thức của {st.session_state.unit_selector} ạ!"

# --- HÀM XỬ LÝ (PHẢI NẰM TRÊN SIDEBAR) ---

def call_ai_now(user_input):
    # Thêm tin nhắn của bé vào lịch sử
    st.session_state.messages.append({"role": "user", "content": user_input})
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[{"role": "user" if m["role"] == "user" else "model", "parts": [{"text": m["content"]}]} for m in st.session_state.messages],
            config=config
        )
        # Lưu câu trả lời của Cô
        st.session_state.messages.append({"role": "model", "content": response.text})
    except Exception as e:
        st.error(f"Cô gặp chút lỗi nhỏ: {e}")

def on_sidebar_action():
    # Kiểm tra xem bé có thực sự chọn bài không
    if st.session_state.unit_selector != "--- Chọn bài ---":
        selected_unit = st.session_state.unit_selector
        call_ai_now(f"Cô ơi, con muốn ôn tập kiến thức của {selected_unit} ạ!")
        # Reset thanh chọn về mặc định để không bị kẹt
        st.session_state.unit_selector = "--- Chọn bài ---"

# --- 7. THANH ĐIỀU KHIỂN BÊN TRÁI (SIDEBAR) ---
with st.sidebar:
    st.title("🎮 Trung tâm học tập")
    
    # PHẦN 1: ÔN TẬP UNIT
    st.write("---")
    st.selectbox(
    "📘 Practice by Unit",
    ["--- Chọn bài ---"] + [f"Unit {i}" for i in range(1, 21)],
    key="unit_selector",
    on_change=on_sidebar_action # Tên này phải giống hệt tên hàm ở Bước 2
)
    
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

# --- 8. KHU VỰC CHÍNH (Tiêu đề & Banner) ---
st.title("👩‍🏫 Gia sư tiếng Anh lớp 5")

# Giữ nguyên dải banner màu tím rực rỡ của con
st.markdown("""
    <div class="top-banner">
        <div>
            <h2 style='margin:0;'>Hello! I'm your English buddy! ⭐</h2>
            <p style='margin:0;'>Cùng học thật vui và trở thành siêu sao tiếng Anh nhé!</p>
        </div>
        <img src="https://cdn-icons-png.flaticon.com/512/3389/3389081.png" width="70">
    </div>
""", unsafe_allow_html=True)

# --- 9. HIỂN THỊ VÀ XỬ LÝ CHAT ---

# 1. Hiển thị lịch sử chat bằng giao diện bong bóng mới (Trái-Phải)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    display_message(msg["role"], msg["content"])
st.markdown('</div>', unsafe_allow_html=True)

# 2. Ô nhập liệu duy nhất
user_input = st.chat_input("Con gõ câu trả lời hoặc thắc mắc vào đây nhé...")

# 3. Kiểm tra lệnh từ nút bấm Sidebar hoặc ô Chat (Giữ chức năng nav_prompt)
final_prompt = None

if "nav_prompt" in st.session_state:
    final_prompt = st.session_state.nav_prompt
    del st.session_state.nav_prompt
elif user_input:
    final_prompt = user_input

# 4. Xử lý khi có tin nhắn mới
if final_prompt:
    # Hiện tin nhắn của con ngay lập tức bằng giao diện mới (Bên TRÁI)
    display_message("user", final_prompt)
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    
    # Cô AI phản hồi kèm vòng quay chờ đợi
    with st.spinner("Cô đang chuẩn bị bài cho con, chờ Cô 1 xíu nhé... ✨"):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=[{"role": "user" if m["role"] == "user" else "model", "parts": [{"text": m["content"]}]} for m in st.session_state.messages],
                config=config
            )
            ai_reply = response.text
            # Hiện câu trả lời của Cô (Bên PHẢI)
            display_message("model", ai_reply)
            # Lưu vào bộ nhớ
            st.session_state.messages.append({"role": "model", "content": ai_reply})
            
            # Lưu xong thì Rerun để chốt vị trí bong bóng chat
            st.rerun()
            
        except Exception as e:
            st.error(f"Lỗi rồi con ơi: {e}")
