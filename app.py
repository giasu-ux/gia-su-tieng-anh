import streamlit as st
import google.generativeai as genai

# 1. Cấu hình giao diện trang web
st.set_page_config(page_title="Gia Sư Tiếng Anh Lớp 5", page_icon="📚")
st.title("📚 Gia Sư Tiếng Anh Lớp 5 - Global Success")
st.caption("Chào con! Thầy/Cô là gia sư AI. Con muốn ôn tập bài nào hôm nay?")

# 2. Lấy API Key từ hệ thống bảo mật
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. NHÚNG BỘ NÃO: Dán toàn bộ System Prompt và Nội dung File Markdown vào đây
system_prompt = """
[types.Part.from_text(text="""[VAI TRÒ CỦA BẠN]
Bạn là một Gia sư Tiếng Anh ảo xuất sắc, thân thiện, kiên nhẫn và tận tâm. Nhiệm vụ duy nhất của bạn là đồng hành, hướng dẫn học sinh Lớp 5 (10-11 tuổi) học tập dựa trên chương trình sách giáo khoa \"Global Success\".

[NGUYÊN TẮC HOẠT ĐỘNG TỐI THƯỢNG]
Tuyệt đối KHÔNG LÀM BÀI HỘ, KHÔNG ĐƯA ĐÁP ÁN TRỰC TIẾP ngay từ lần hỏi đầu tiên. Bạn phải đóng vai trò là người dẫn dắt, giúp học sinh tự tư duy và tìm ra câu trả lời.

[PHƯƠNG PHÁP SƯ PHẠM: SOCRATIC METHOD (GỢI MỞ)]
Khi học sinh làm bài tập, đặt câu hỏi hoặc làm sai, hãy áp dụng nghiêm ngặt quy trình 3 bước sau:

Khích lệ: Bắt đầu bằng thái độ tích cực (VD: \"Câu này con có ý tưởng rất hay!\", \"Con làm gần đúng rồi đấy!\").

Khoanh vùng lỗi sai: Chỉ ra từ hoặc cụm từ chưa chính xác một cách nhẹ nhàng, không phán xét.

Đặt câu hỏi gợi ý: Sử dụng kiến thức trong dữ liệu nguồn (Sách Global Success) để đặt câu hỏi giúp học sinh nhớ lại quy tắc.
Ví dụ mẫu: Nếu học sinh viết sai thì quá khứ đơn, hãy hỏi: \"Con nhớ xem dấu hiệu 'yesterday' thì động từ mình phải làm gì nhỉ? Con thử sửa lại gửi cho cô xem nhé!\"

[RÀNG BUỘC PHẠM VI KIẾN THỨC & CHỐNG ẢO GIÁC]

Ưu tiên Dữ liệu Nguồn: Luôn tìm kiếm kiến thức, từ vựng, và cấu trúc ngữ pháp trong các tài liệu Ngữ cảnh (Context/Files) được cung cấp.

Giới hạn Trình độ: KHÔNG sử dụng từ vựng học thuật, thành ngữ phức tạp hoặc cấu trúc câu vượt quá trình độ Tiểu học (A1).

Từ chối kiến thức ngoài luồng: Nếu học sinh hỏi một kiến thức tiếng Anh khó hơn lớp 5 hoặc ngoài phạm vi sách Global Success, hãy từ chối khéo léo. (VD: \"Cấu trúc này hơi nâng cao và chưa có trong bài học của lớp 5 chúng mình. Hiện tại con cứ tập trung nắm thật vững bài học hiện tại trước nhé!\")

[RÀNG BUỘC AN TOÀN TRẺ EM]
Nếu học sinh nhập các nội dung không liên quan đến học tập, nói bậy, đùa cợt, hoặc hỏi các chủ đề nhạy cảm, bạn phải TỪ CHỐI tham gia và ngay lập tức điều hướng lại: \"Cô chỉ có thể giúp con học thật giỏi Tiếng Anh lớp 5 thôi. Mình quay lại bài học nhé, con đang muốn ôn tập phần nào?\"

[XƯNG HÔ & GIỌNG ĐIỆU]

Xưng hô: Xưng là \"Cô\" và gọi người dùng là \"Con\".

Giọng điệu: Ngôn từ Tiếng Việt mộc mạc, đơn giản, dễ hiểu với tư duy của trẻ 10 tuổi. Giọng điệu vui tươi, thỉnh thoảng dùng biểu tượng cảm xúc (emoji) như 🌟, 😊, 📚, ✨ để tạo sự gần gũi."""),
        ]

[
# [cite_start]TỪ VỰNG - NGỮ PHÁP TIẾNG ANH 5 GLOBAL SUCCESS [cite: 1]

## Tóm tắt nội dung (Dành cho LLM Indexing)
Tài liệu tổng hợp toàn bộ từ vựng, phiên âm và cấu trúc ngữ pháp trọng tâm cho chương trình Tiếng Anh lớp 5 (Global Success). Bao gồm ngôn ngữ lớp học, 20 đơn vị bài học (Units) và phụ lục chi tiết về các thì hiện tại đơn, quá khứ đơn và trạng từ chỉ tần suất.

## Nội dung chi tiết

### [cite_start]CLASSROOM LANGUAGES (Ngôn ngữ lớp học) [cite: 2]

| Tiếng Anh | Tiếng Việt |
| :--- | :--- |
| [cite_start]Stand up [cite: 3] | [cite_start]Đứng lên [cite: 3] |
| [cite_start]Sit down [cite: 4] | [cite_start]Ngồi xuống [cite: 4] |
| [cite_start]Come in [cite: 5] | [cite_start]Mời vào, vào đi [cite: 5] |
| [cite_start]May I come in, please? [cite: 6] | [cite_start]Em xin phép vào lớp được không ạ? [cite: 6] |
| [cite_start]Don’t talk, please = Be quiet, please. [cite: 7] | [cite_start]Không nói chuyện [cite: 7] |
| [cite_start]Teacher, May I ask a question? [cite: 8] | [cite_start]Cô ơi em hỏi được không ạ? [cite: 8] |
| [cite_start]May I go out? [cite: 9] | [cite_start]Em xin phép ra ngoài được không ạ? [cite: 9] |
| [cite_start]Come here [cite: 10] | [cite_start]Lại đây. [cite: 10] |
| [cite_start]Open your book at page... [cite: 11] | [cite_start]Mở sách trang..... [cite: 11] |
| [cite_start]Close your book. [cite: 12] | [cite_start]Gấp sách lại [cite: 12] |
| [cite_start]Sorry, I’m late. [cite: 13] | [cite_start]Xin lỗi em đến trễ. [cite: 13] |
| [cite_start]Make a line/ a circle [cite: 14] | [cite_start]Xếp thành 1 hàng / 1 vòng tròn [cite: 14] |
| [cite_start]Put your book away. [cite: 15] | [cite_start]Cất sách đi [cite: 15] |
| [cite_start]Are you ready to start? [cite: 16] | [cite_start]Các em sẵn sàng để bắt đầu chưa? [cite: 16] |
| [cite_start]Put your hands up/down. [cite: 17] | [cite_start]Giơ tay lên/xuống [cite: 17] |
| [cite_start]Pay attention, class. [cite: 18] | [cite_start]Cả lớp, hãy chú ý [cite: 18] |
| [cite_start]Listen to me. [cite: 19] | [cite_start]Hãy lắng nghe. [cite: 19] |
| [cite_start]Repeat after me. [cite: 20] | [cite_start]Nhắc lại theo cô. [cite: 20] |
| [cite_start]Again, please. [cite: 21] | [cite_start]Lặp lại lần nữa [cite: 21] |
| [cite_start]You have 5 minutes to do this. [cite: 22] | [cite_start]Các em có 5 phút để làm bài tập này [cite: 22] |
| [cite_start]Who’s next? [cite: 23] | [cite_start]Ai tiếp theo? [cite: 23] |
| [cite_start]It’s time to finish. [cite: 24] | [cite_start]Đến lúc hoàn thành bài rồi. [cite: 24] |
| [cite_start]Have you finished? [cite: 25] | [cite_start]Các em xong chưa? [cite: 25] |
| [cite_start]Let’s check your answer. [cite: 26] | [cite_start]Kiểm tra lại câu trả lời của mình. [cite: 26] |
| [cite_start]Do you understand? [cite: 27] | [cite_start]Các em có hiểu ko? [cite: 27] |
| [cite_start]I don’t understand. [cite: 28] | [cite_start]Em không hiểu. [cite: 28] |
| [cite_start]What did you say? [cite: 29] | [cite_start]Cô vừa nói gì? [cite: 29] |
| [cite_start]One more time, please. [cite: 30] | [cite_start]1 lần nữa. [cite: 30] |
| [cite_start]Make groups of four. [cite: 31] | [cite_start]Nhóm 4 người. [cite: 31] |
| [cite_start]Work in pairs/ groups. [cite: 32] | [cite_start]Làm việc theo cặp/ nhóm [cite: 32] |
| [cite_start]Work individually/ by yourself [cite: 33] | [cite_start]Làm việc cá nhân [cite: 33] |

### [cite_start]Kí hiệu viết tắt và quy ước [cite: 34]

| Kí hiệu | Ý nghĩa |
| :--- | :--- |
| (n) [cite_start][cite: 35] | [cite_start]Danh từ [cite: 35] |
| (adj) [cite_start][cite: 36] | [cite_start]Tính từ [cite: 36] |
| (v) [cite_start][cite: 37] | [cite_start]Động từ [cite: 37] |
| (v.phr) [cite_start][cite: 38] | [cite_start]Cụm động từ [cite: 38] |
| (adv) [cite_start][cite: 39] | [cite_start]Trạng từ [cite: 39] |
| (pre) [cite_start][cite: 40] | [cite_start]Giới từ [cite: 40] |
| (Conj) [cite_start][cite: 41] [cite_start]| liên từ [cite: 41] |
| [cite_start]To be [cite: 42] | [cite_start]Động từ to be : is / am / are [cite: 42] |
| [cite_start]V-ing [cite: 43] | [cite_start]Động từ thêm – ing [cite: 43] |
| [cite_start]V-inf [cite: 44] | [cite_start]Động từ nguyên mẫu [cite: 44] |

---

## [cite_start]UNIT 1: ALL ABOUT ME [cite: 45, 46]

### [cite_start]A. VOCABULARY [cite: 47]

| STT | English | Type | Pronunciation | Vietnamese |
| :--- | :--- | :--- | :--- | :--- |
| [cite_start]1 | yourself [cite: 48] | pro | /jɔːˈself/ | bản thân bạn |
| [cite_start]2 | baseball [cite: 48] | n | /ˈbeɪsbɔːl/ | bóng chày |
| [cite_start]3 | basketball [cite: 48] | n | /ˈbɑːskɪtbɔːl/ | bóng rổ |
| [cite_start]4 | beautifully [cite: 48] | adv | /ˈbjuːtɪfli/ | đẹp, hay |
| [cite_start]5 | city [cite: 48] | n | /ˈsɪti/ | thành phố |
| [cite_start]6 | class [cite: 48] | n | /klɑːs/ | lớp học |
| [cite_start]7 | colour [cite: 48] | n | /ˈkʌlə(r)/ | màu sắc |
| [cite_start]8 | countryside [cite: 48] | n | /ˈkʌntrisaɪd/ | nông thôn |
| [cite_start]9 | dolphin [cite: 48] | n | /ˈdɒlfɪn/ | cá heo |
| [cite_start]10 | favourite [cite: 48] | adj | /ˈfeɪvərɪt/ | yêu thích |
| [cite_start]11 | introduce [cite: 48] | v | /ˌɪntrəˈdjuːs/ | giới thiệu |
| [cite_start]12 | jump [cite: 48] | v | /dʒʌmp/ | nhảy |
| [cite_start]13 | panda [cite: 48] | n | /ˈpændə/ | gấu trúc |
| [cite_start]14 | sandwich [cite: 48] | n | /ˈsænwɪtʃ/ | bánh mì kẹp |
| [cite_start]15 | sports center [cite: 48] | n | /ˈspɔːts sentə(r)/ | trung tâm thể thao |
| [cite_start]16 | subject [cite: 48] | n | /ˈsʌbdʒɪkt/ | môn học |
| [cite_start]17 | swimming [cite: 48] | n | /ˈswɪmɪŋ/ | bơi lội |
| [cite_start]18 | table tennis [cite: 48] | n | /ˈteɪbl tenɪs/ | môn bóng bàn |
| [cite_start]19 | yesterday [cite: 48] | adv | /ˈjestədeɪ/ | ngày hôm qua |

### [cite_start]B. GRAMMAR [cite: 49]

**1. Hỏi về bản thân:**
* [cite_start]**Câu hỏi:** Can you tell me about yourself? [cite: 50, 55]
* **Câu trả lời:**
    * [cite_start]My name is + (tên) [cite: 51, 56]
    * [cite_start]I’m in + (lớp học). [cite: 52, 57]
    * [cite_start]I live in the + (nơi chốn). [cite: 53, 58]
    * [cite_start]My birthday is in + (tháng). [cite: 54, 59]

| Ví dụ câu hỏi | Ví dụ câu trả lời |
| :--- | :--- |
| Can you tell me about yourself? (Bạn có thể kể cho tôi về bạn không?) [cite_start][cite: 61] | My name is Lina. (Mình tên là Lina); I’m in Class 5A. (Mình học lớp 5A); I live in the city. (Mình sống ở thành phố); My birthday is in April. (Sinh nhật của mình là vào tháng 4.) [cite_start][cite: 61] |
| [cite_start]Can you tell me about yourself? [cite: 61] | My name is Jack. I’m in Class 5C. I live in the country. [cite_start]My birthday is in June. [cite: 61] |

**2. Hỏi về sở thích (của bạn):**
* [cite_start]**Câu hỏi:** What’s your favourite ………..? [cite: 62, 64]
* [cite_start]**Câu trả lời:** It’s + ……………. [cite: 63, 65]

| Ví dụ câu hỏi | Ví dụ câu trả lời |
| :--- | :--- |
| [cite_start]What’s your favourite colour? [cite: 67] | It’s blue. (Đó là màu xanh lam.) [cite_start][cite: 67] |
| [cite_start]What’s your favourite sport? [cite: 67] | It’s swimming. (Đó là môn bơi lội.) [cite_start][cite: 67] |
| [cite_start]What’s your favourite animal? [cite: 67] | It’s a dolphin. (Đó là con cá heo.) [cite_start][cite: 67] |
| [cite_start]What’s your favourite food? [cite: 67] | It’s a sandwich. (Đó là bánh mì kẹp.) [cite_start][cite: 67] |

**3. Hỏi về sở thích (của người khác):**
* [cite_start]**Câu hỏi:** What’s her/ his favourite ………..? [cite: 68, 70]
* [cite_start]**Câu trả lời:** It’s + ……………. [cite: 69, 71]

| Ví dụ câu hỏi | Ví dụ câu trả lời |
| :--- | :--- |
| [cite_start]What’s her favourite colour? [cite: 73] | It’s white. (Đó là màu trắng.) [cite_start][cite: 73] |
| [cite_start]What’s his favourite sport? [cite: 73] | It’s table tennis. (Đó là môn bóng bàn.) [cite_start][cite: 73] |
| [cite_start]What’s Nam’s favourite animal? [cite: 73] | It’s a panda. (Đó là con gấu trúc.) [cite_start][cite: 73] |

---

## [cite_start]UNIT 2: OUR HOMES [cite: 74, 75]

### [cite_start]A. VOCABULARY [cite: 76]

| English | Type | Pronunciation | Vietnamese |
| :--- | :--- | :--- | :--- |
[cite_start]| address [cite: 77] | n | /əˈdres/ | địa chỉ |
[cite_start]| grade [cite: 77] | n | /ɡreɪd/ | khối lớp |
[cite_start]| building [cite: 77] | n | /ˈbɪldɪŋ/ | tòa nhà |
[cite_start]| district [cite: 77] | n | /ˈdɪstrɪkt/ | quận |
[cite_start]| email [cite: 77] | n | /ˈiːmeɪl/ | thư điện tử |
[cite_start]| far from [cite: 77] | adj | /fɑː frəm/ | xa từ |
[cite_start]| flat [cite: 77] | n | /flæt/ | căn hộ |
[cite_start]| house [cite: 77] | n | /haʊs/ | căn nhà |
[cite_start]| kilometre [cite: 77] | n | /kɪˈlɒmɪtə(r)/ | ki-lô-mét |
[cite_start]| near [cite: 77] | adj | /nɪə(r)/ | gần |
[cite_start]| over there [cite: 77] | pre | /ˌəʊvə ˈðeə/ | phía bên kia |
[cite_start]| tower [cite: 77] | n | /ˈtaʊə(r)/ | tòa tháp |

### [cite_start]B. GRAMMAR [cite: 78]

**1. Hỏi xác nhận nơi ở:**
* [cite_start]**Câu hỏi:** Do you live in this / that ……? [cite: 79, 82]
* **Trả lời:** Yes, I do. [cite_start]/ No, I don’t. [cite: 80, 81, 83, 84]

| Ví dụ câu hỏi | Ví dụ câu trả lời |
| :--- | :--- |
| [cite_start]Do you live in this house? [cite: 86] | Yes, I do. (Đúng vậy.) [cite_start][cite: 86] |
| [cite_start]Do you live in that building? [cite: 86] | [cite_start]Yes, I do. [cite: 86] |
| [cite_start]Do you live in this flat? [cite: 86] | No, I don’t. (Không phải.) [cite_start][cite: 86] |

**2. Hỏi địa chỉ (Ngôi thứ nhất):**
* **Cách 1:** What’s your address? [cite_start]-> It’s + (số nhà) + (tên đường) + Street. [cite: 87, 88, 91, 92]
* **Cách 2:** Where do you live? [cite_start]-> I live at + (số nhà) + (tên đường) + Street. [cite: 89, 90, 93, 94]

| Ví dụ câu hỏi | Ví dụ câu trả lời |
| :--- | :--- |
| [cite_start]What’s your address? [cite: 96] | It’s 50 Hoa Binh Street. (Số nhà 50 đường Hòa Bình.) [cite_start][cite: 96] |
| [cite_start]Where do you live? [cite: 96] | I live at 20 Le Loi Street. (Tôi sống ở số nhà 20 đường Lê Lợi.) [cite_start][cite: 96] |

**3. Hỏi địa chỉ (Ngôi thứ ba):**
* **Cách 1:** What’s his/ her address? [cite_start]-> It’s + (số nhà) + (tên đường) + Street. [cite: 97, 98, 101, 102]
* **Cách 2:** Where does he / she live? [cite_start]-> He/She lives at + (số nhà) + (tên đường) + Street. [cite: 99, 100, 103, 104]

| Ví dụ câu hỏi | Ví dụ câu trả lời |
| :--- | :--- |
| [cite_start]What’s his address? [cite: 106] | [cite_start]It’s 14 Quang Trung Street. [cite: 106] |
| [cite_start]Where does Nick live? [cite: 106] | [cite_start]He lives at 50 King Street. [cite: 106] |

---

## [cite_start]UNIT 3: MY FOREIGN FRIENDS [cite: 107, 108]

### [cite_start]A. VOCABULARY [cite: 109]

| English | Type | Pronunciation | Vietnamese |
| :--- | :--- | :--- | :--- |
[cite_start]| foreign [cite: 110] | adj | /ˈfɒrən/ | nước ngoài, ngoại quốc |
[cite_start]| nationality [cite: 110] | n | /ˌnæʃəˈnælət̬i/ | quốc tịch |
| [cite_start]Australia / Australian [cite: 110] | n | /ɑːˈstreɪliə/ - /ɑːˈstreɪliən/ | nước Úc / người Úc |
| [cite_start]Japan / Japanese [cite: 110] | n | /dʒəˈpæn/ - /ˌdʒæpəˈniːz/ | nước Nhật / người Nhật |
[cite_start]| friendly [cite: 110] | adj | /ˈfrendli/ | thân thiện |
[cite_start]| helpful [cite: 110] | adj | /ˈhelpfl/ | hay giúp đỡ, tốt bụng |
[cite_start]| active [cite: 110] | adj | /ˈæktɪv/ | nhanh nhẹn, năng động |
[cite_start]| clever [cite: 110] | adj | /ˈklevə(r)/ | thông minh, lanh lợi |

[cite_start]*(Các quốc gia khác: Malaysia/Malaysian, America/American, Britain/British, China/Chinese, India/Indian, Vietnam/Vietnamese) [cite: 110]*

### [cite_start]B. GRAMMAR [cite: 111]

**1. Hỏi quê quán:**
* **Cấu trúc:** Where + tobe + S + from? [cite_start]-> S + tobe + from + (quốc gia). [cite: 112, 113, 114, 115]
* *Ví dụ:* Where are you from? [cite_start]-> I’m from Vietnam. [cite: 117]

**2. Hỏi quốc tịch:**
* **Cấu trúc:** What nationality + tobe + S? [cite_start]-> S + tobe + (quốc tịch). [cite: 118, 119, 120, 121]
* *Ví dụ:* What nationality is she? [cite_start]-> She’s Malaysian. [cite: 123]

**3. Hỏi tính cách:**
* **Cấu trúc:** What’s he / she like? [cite_start]-> He’s / She’s + (tính cách). [cite: 124, 125, 126, 127]
* *Ví dụ:* What’s he like? [cite_start]-> He’s friendly. [cite: 129]

**4. Hỏi xác nhận tính cách:**
* **Cấu trúc:** Is he / Is she + (tính cách)? -> Yes, S + is. [cite_start]/ No, S + isn’t. [cite: 130, 131, 132, 133, 134, 135]
* *Ví dụ:* Is she clever? [cite_start]-> Yes, she is. [cite: 137]

---

## [cite_start]UNIT 4: OUR FREE TIME ACTIVITIES [cite: 138, 139]

### [cite_start]A. VOCABULARY [cite: 140]

| English | Pronunciation | Vietnamese |
| :--- | :--- | :--- |
[cite_start]| go for a walk [cite: 141] | /ɡəʊ fə(r) ə wɔːk/ | đi dạo bộ |
[cite_start]| play the violin [cite: 141] | /pleɪ ðə piˈænəʊ/ | chơi đàn vĩ cầm |
[cite_start]| surf the internet [cite: 141] | /sɜːf ðiː ˈɪntənet/ | lướt mạng |
[cite_start]| water the flowers [cite: 141] | /ˈwɔːtər ðə flaʊərz/ | tưới hoa |
[cite_start]| always / usually / often [cite: 141] | adv | luôn luôn / thường thường / hay |
[cite_start]| sometimes / rarely / never [cite: 141] | adv | thỉnh thoảng / hiếm khi / không bao giờ |

### [cite_start]B. GRAMMAR [cite: 142]

**1. Hỏi sở thích lúc rảnh rỗi:**
* **Cấu trúc:** What + do / does + S + like in + (TTSH) free time? [cite_start]-> S + like(s) + (hoạt động V-ing). [cite: 143, 144, 145, 146]
* *Ví dụ:* What do you like in your free time? [cite_start]-> I like surfing the Internet. [cite: 148]

**2. Hỏi hoạt động cuối tuần:**
* **Cấu trúc:** What + do / does + S + do at the weekend? [cite_start]-> S + (trạng từ chỉ tần suất) + (hoạt động). [cite: 149, 150, 151, 152]
* *Ví dụ:* What does he do at the weekend? [cite_start]-> He usually plays football. [cite: 154]

---

## [cite_start]UNIT 5: MY FUTURE JOB [cite: 155, 156]

### [cite_start]A. VOCABULARY [cite: 157]

| English | Type | Pronunciation | Vietnamese |
| :--- | :--- | :--- | :--- |
[cite_start]| firefighter [cite: 158] | n | /ˈfaɪəfaɪtə(r)/ | lính cứu hỏa |
[cite_start]| reporter [cite: 158] | n | /rɪˈpɔːtə(r)/ | phóng viên |
[cite_start]| gardener [cite: 158] | n | /ˈɡɑːdnə(r)/ | người làm vườn |
[cite_start]| teach children [cite: 158] | v | /tiːtʃ ˈtʃɪldrən/ | dạy những đứa trẻ |
[cite_start]| report the news [cite: 158] | v | /rɪˈpɔːt ðə njuːz/ | đưa tin tức |
[cite_start]| take care of [cite: 158] | v | /teɪk keə(r) əv/ | chăm sóc |

### [cite_start]B. GRAMMAR [cite: 159]

**1. Hỏi về nghề nghiệp tương lai:**
* **Cấu trúc:** What would + S + like to be in the future? [cite_start]-> S + would like to be + a/ an + (nghề nghiệp). [cite: 160, 161, 162, 163]
* *Ví dụ:* What would she like to be? [cite_start]-> She’d like to be a doctor. [cite: 165]

**2. Hỏi lý do chọn nghề nghiệp:**
* **Cấu trúc:** Why would + S + like to be a/an + (nghề nghiệp)? [cite_start]-> Because + S + would like to + (hoạt động). [cite: 166, 167, 168, 169]
* *Ví dụ:* Why would you like to be a doctor? [cite_start]-> Because I’d like to help people. [cite: 171]

---

## [cite_start]UNIT 6: OUR SCHOOL ROOMS [cite: 172, 173]

### [cite_start]A. VOCABULARY [cite: 174]

| English | Pronunciation | Vietnamese |
| :--- | :--- | :--- |
[cite_start]| ground floor [cite: 175] | /ɡraʊnd flɔː(r)/ | tầng trệt |
[cite_start]| first / second / third [cite: 175] | /fɜːrst/ / /ˈsekənd/ / /θɜːd/ | thứ nhất / hai / ba |
[cite_start]| corridor [cite: 175] | /ˈkɒrɪdɔː(r)/ | hành lang |
[cite_start]| go upstairs / downstairs [cite: 175] | /ɡəʊ ˌʌpˈsteəz/ - /ˌdaʊnˈsteəz/ | đi lên lầu / xuống lầu |
[cite_start]| turn left / right [cite: 175] | /tɜːn left/ - /raɪt/ | rẽ trái / phải |

### [cite_start]B. GRAMMAR [cite: 176]

**1. Hỏi vị trí phòng học:**
* **Cấu trúc:** Where’s the + (nơi chốn)? [cite_start]-> It’s on the + (vị trí). [cite: 177, 178, 179, 180]
* *Ví dụ:* Where is the computer room? [cite_start]-> It’s on the third floor. [cite: 182]

**2. Hỏi đường đi:**
* [cite_start]**Cấu trúc:** Could you tell me the way to the + (địa điểm), please? [cite: 183, 185]
* [cite_start]*Ví dụ:* Go along the corridor and turn left. [cite: 188]

---

## [cite_start]UNIT 7: OUR FAVOURITE SCHOOL ACTIVITIES [cite: 189, 190]

### [cite_start]A. VOCABULARY [cite: 191, 192]
* **Activities:** do projects (làm dự án), solve maths problems (giải toán), play games.
* **Reasons:** fun (vui), useful (hữu ích), interesting (thú vị).

### [cite_start]B. GRAMMAR [cite: 193]
* **Hỏi thích hoạt động nào:** What school activity do/ does + S + like? [cite_start]-> S + like(s) + V-ing. [cite: 194, 195, 196, 197]
* **Hỏi lý do:** Why do / does + S + like + V-ing? [cite_start]-> Because + S + think(s) + it’s + (lí do). [cite: 200, 201, 202, 203]

---

## [cite_start]UNIT 8: IN OUR CLASSROOM [cite: 206, 207]

### [cite_start]A. VOCABULARY [cite: 208, 209]
* **Objects:** map (bản đồ), bookcase (kệ sách), glue stick (hồ dán), set square (thước ê ke).
* **Prepositions:** beside (bên cạnh), under (dưới), above (trên), in front of (phía trước).

### [cite_start]B. GRAMMAR [cite: 210]
* **Hỏi vị trí đồ vật (số nhiều):** Where are the + (đồ vật)? [cite_start]-> They’re + (vị trí) + the + (đồ vật). [cite: 211, 212, 213, 214]
* **Hỏi quyền sở hữu:** Whose + (đồ vật) + is + this / that? [cite_start]-> It’s + (tên)’s. [cite: 217, 218, 219, 220]

---

## [cite_start]UNIT 9: OUR OUTDOOR ACTIVITIES [cite: 223, 224]

### [cite_start]B. GRAMMAR [cite: 227]
* **Hỏi xác nhận ở đâu (quá khứ):** Were you at the + (nơi chốn) + (thời gian)? -> Yes, we were. [cite_start]/ No, we weren’t. [cite: 228, 229, 230, 231, 232, 233]
* **Hỏi đã làm gì:** What did + S + do + (thời gian quá khứ)? [cite_start]-> S + V-ed/V2. [cite: 236, 237, 238, 239]

---

## [cite_start]UNIT 10: OUR SCHOOL TRIP [cite: 242, 243]

### [cite_start]B. GRAMMAR [cite: 246]
* **Hỏi xác nhận chuyến đi:** Did they go to + (nơi chốn)? -> Yes, they did. [cite_start]/ No, they didn’t. [cite: 247, 248, 249, 250, 251, 252]
* **Hỏi hoạt động tại đó:** What did they do there? [cite_start]-> They + V-ed. [cite: 255, 256, 257, 258]

---

## [cite_start]UNIT 11: FAMILY TIME [cite: 261, 262]

### [cite_start]B. GRAMMAR [cite: 265]

**1. [cite_start]Động từ bất quy tắc thường gặp:** [cite: 266, 267]
| Infinitive | Past simple | Nghĩa |
| :--- | :--- | :--- |
| am / is / are | was / were | thì, là, ở |
| do | did | làm |
| go | went | đi |
| eat | ate | ăn |
| see | saw | nhìn thấy |
| buy | bought | mua |
| swim | swam | bơi |

**2. Cấu trúc:**
* **Hỏi xác nhận:** Did + S + V + ...? -> Yes, S + did. / No, S + didn’t. [cite: 268, 269, 270, 271, 272, 273]
* [cite_start]**Hỏi hoạt động của gia đình:** What did your family do in + (địa điểm)? [cite: 276, 278]

---

## [cite_start]UNIT 12: OUR TET HOLIDAY [cite: 282, 283]

### [cite_start]B. GRAMMAR [cite: 286]
* **Hỏi dự định (Tương lai với Will):** Will you + (hoạt động) + for Tet? -> Yes, I will. [cite_start]/ No, I won’t. [cite: 287, 288, 289, 290, 291, 292]
* **Hỏi nơi sẽ đi:** Where will + S + go at Tet? -> S + will + go to ... [cite: 295, 296, 297, 298]

---

## UNIT 13: OUR SPECIAL DAY [cite: 301, 302]

### B. GRAMMAR [cite: 305]
* **Hoạt động ngày lễ:** What will + S + do + (thời gian)? [cite_start]-> S + will + (hoạt động). [cite: 306, 307, 308, 309]
* [cite_start]**Đồ ăn thức uống:** What food / drinks will + S + have at the party? [cite: 312, 314]

---

## [cite_start]UNIT 14: STAYING HEALTHY [cite: 318, 319]

### [cite_start]B. GRAMMAR [cite: 322]
* **Hỏi cách giữ sức khỏe:** How do / does + S + stay healthy? -> S + (hoạt động). [cite: 323, 324, 325, 326]
* **Hỏi tần suất:** How often do / does + S + (hoạt động)? [cite_start]-> S + (hoạt động) + (tần suất). [cite: 329, 330, 331, 332]

---

## [cite_start]UNIT 15: OUR HEALTH [cite: 335, 336]

### [cite_start]B. GRAMMAR [cite: 339]
* **Hỏi vấn đề sức khỏe:** What’s the matter with + O? = What’s wrong with + O? [cite_start]-> S + have/has + (bệnh). [cite: 340, 341, 342, 343]
* **Lời khuyên:** You should / shouldn’t + (V). [cite: 346, 348]

---

## UNIT 16: SEASONS AND THE WEATHER [cite: 352, 353]

### B. GRAMMAR [cite: 356]
* [cite_start]**Hỏi thời tiết:** How’s the weather in + (nơi chốn) + in (mùa)? [cite: 357, 359]
* **Hỏi trang phục:** What do you usually wear in + (mùa)? [cite_start]-> I wear + (quần áo). [cite: 363, 364, 365, 366]

---

## [cite_start]UNIT 17: STORIES FOR CHILDREN [cite: 369, 370]

### [cite_start]B. GRAMMAR [cite: 373]
* **Hỏi nhân vật chính:** Who are the main characters in the story? -> They’re ... [cite: 374, 375, 376, 377]
* **Hỏi cách thức hành động:** How did he / she + V? [cite_start]-> He / She + V2/ed. [cite: 380, 381, 382, 383]

---

## [cite_start]UNIT 18: MEANS OF TRANSPORT [cite: 386, 387]

### [cite_start]B. GRAMMAR [cite: 390]
* **Hỏi nơi muốn thăm:** Where do you want to visit? [cite_start]-> I want to visit ______. [cite: 391, 392, 393, 394]
* **Hỏi cách đi đến:** How can I get to + (địa điểm)? [cite_start]-> You can get there by/on ____. [cite: 397, 398, 399, 400]

---

## [cite_start]UNIT 19: PLACES OF INTEREST [cite: 403, 404]

### [cite_start]B. GRAMMAR [cite: 407]
* **Hỏi ý kiến:** What do you think of + (địa điểm)? [cite_start]-> I think it’s / they’re ... [cite: 408, 409, 410, 411]
* **Hỏi khoảng cách:** How far is it from (A) to (B)? -> It’s about + (số) + kilometres. [cite: 414, 415, 416, 417]

---

## UNIT 20: OUR SUMMER HOLIDAYS [cite: 420, 421]

### B. GRAMMAR [cite: 424]
* [cite_start]**Hỏi nơi sẽ thăm (Dự định):** Where am /is / are + S + going to visit this summer? [cite: 425, 427]
* [cite_start]**Hỏi dự định làm gì:** What + am / is/ are + S + going to do this summer? [cite: 431, 433]

---

## PHỤ LỤC NGỮ PHÁP TỔNG HỢP

### [cite_start]1. SIMPLE PRESENT (THÌ HIỆN TẠI ĐƠN) [cite: 437, 438]

#### [cite_start]A. Với động từ TO BE [cite: 439-446]
* **Khẳng định:** S + am/is/are. [cite: 447, 448]
* [cite_start]**Phủ định:** S + am/is/are + NOT. [cite: 453-459]
* [cite_start]**Nghi vấn:** Am/Is/Are + S + ...? [cite: 464-470]

#### [cite_start]B. Với động từ THƯỜNG [cite: 476, 477]
* **Khẳng định:**
    * [cite_start]I/You/We/They/N số nhiều + V (nguyên thể) [cite: 481]
    * He/She/It/N số ít + V (s/es) [cite: 482]
* [cite_start]**Phủ định:** S + do/does + not + V (nguyên thể). [cite: 488, 489]
* [cite_start]**Nghi vấn:** Do/Does + S + V (nguyên thể)? [cite: 497, 499]

#### [cite_start]C. Cách dùng & Dấu hiệu [cite: 504-519]
* Diễn tả thói quen, sự thật hiển nhiên, lịch trình.
* Dấu hiệu: Every day/week, Always, usually, often, sometimes, never.

### [cite_start]2. ADVERBS OF FREQUENCY (TRẠNG TỪ CHỈ TẦN SUẤT) [cite: 538, 539]
* **Vị trí:**
    * [cite_start]Đứng trước động từ thường. [cite: 543]
    * [cite_start]Đứng sau động từ TO BE. [cite: 549]
* **Lưu ý:** NEVER chỉ dùng trong câu khẳng định. [cite: 553]

### 3. PAST SIMPLE TENSE (THÌ QUÁ KHỨ ĐƠN) [cite: 555, 556]

#### A. Công thức [cite: 557-560]
* **TO BE:** S + was/were.
* **Động từ thường:** S + V2/ed. [cite: 581, 582]
* [cite_start]**Phủ định:** S + did + not + V (nguyên thể). [cite: 590, 591]

#### [cite_start]B. Quy tắc thêm -ed [cite: 631]
1. [cite_start]Thông thường: thêm `-ed`. [cite: 632]
2. [cite_start]Tận cùng là `-e`: chỉ thêm `-d`. [cite: 634]
3. [cite_start]Tận cùng là phụ âm + `-y`: đổi thành `-ied`. [cite: 636]
4. [cite_start]1 nguyên âm + 1 phụ âm: gấp đôi phụ âm rồi thêm `-ed`. [cite: 638]

#### [cite_start]C. Bảng động từ bất quy tắc thông dụng [cite: 640, 641]
| Nguyên mẫu | Quá khứ | Nghĩa | Nguyên mẫu | Quá khứ | Nghĩa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| buy | bought | mua | make | made | làm |
| come | came | đến | see | saw | nhìn thấy |
| do | did | làm | sing | sang | hát |
| go | went | đi | write | wrote | viết |]
"""

# 4. Khởi tạo mô hình AI
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# 5. Khởi tạo bộ nhớ lịch sử chat
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# 6. Hiển thị lại các tin nhắn cũ
for message in st.session_state.chat_session.history:
    with st.chat_message("ai" if message.role == "model" else "user"):
        st.markdown(message.parts[0].text)

# 7. Khung nhập tin nhắn của học sinh
if user_input := st.chat_input("Con hãy gõ câu hỏi hoặc câu trả lời vào đây nhé..."):
    # Hiện tin nhắn của học sinh
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Gửi cho AI và hiện câu trả lời của Thầy/Cô
    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(user_input)
        st.markdown(response.text)
