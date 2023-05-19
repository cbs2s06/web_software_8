from flask import Flask, render_template, request, redirect, url_for
import os
import openai
import pdfplumber # 用於處理PDF文件
import re # 用於使用正則表達式

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health.html')
def health():
    return render_template('health.html')

@app.route('/forum_index')
def forum_index():
    return render_template('forum_index.html')

@app.route('/forum_post1.html')
def forum_post1():
    return render_template('forum_post1.html')

@app.route('/forum_post2.html')
def forum_post2():
    return render_template('forum_post2.html')

@app.route('/forum_post3.html')
def forum_post3():
    return render_template('forum_post3.html')

@app.route('/forum_post4.html')
def forum_post4():
    return render_template('forum_post4.html')

@app.route('/forum_post5.html')
def forum_post5():
    return render_template('forum_post5.html')

@app.route('/index.html')
def index_default():
    return render_template('index.html')

@app.route('/translation_default.html')
def index_translation_default():
    return render_template('translation_default.html')

@app.route('/translation_cambodia.html')
def index_translation_cambodia():
    return render_template('translation_cambodia.html')

@app.route('/translation_india.html')
def index_translation_india():
    return render_template('translation_india.html')

@app.route('/translation_indonesia.html')
def index_translation_indonesia():
    return render_template('translation_indonesia.html')

@app.route('/translation_japan.html')
def index_translation_japan():
    return render_template('translation_japan.html')

@app.route('/translation_korea.html')
def index_translation_korea():
    return render_template('translation_korea.html')

@app.route('/translation_laos.html')
def index_translation_laos():
    return render_template('translation_laos.html')

@app.route('/translation_malaysia.html')
def index_translation_malaysia():
    return render_template('translation_malaysia.html')

@app.route('/translation_myanmar.html')
def index_translation_myanmar():
    return render_template('translation_myanmar.html')

@app.route('/translation_philippines.html')
def index_translation_philippines():
    return render_template('translation_philippines.html')

@app.route('/translation_thailand.html')
def index_translation_thailand():
    return render_template('translation_thailand.html')

@app.route('/translation_uk.html')
def index_translation_uk():
    return render_template('translation_uk.html')

@app.route('/translation_vietnam.html')
def index_translation_vietnam():
    return render_template('translation_vietnam.html')

@app.route('/convert_vietnam', methods=['POST'])
def convert_vietnam():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
            Bạn là một thông dịch viên cung cấp dịch vụ tình nguyện thông dịch trong lớp học cho học sinh tiểu học cư dân mới đến từ nước ngoài ở Đài Loan.

            Hai từ đầu tiên của tin nhắn văn bản Trung Quốc gửi cho bạn là tên đối tượng tương ứng với tiếng Trung Quốc, bạn có thể biết đó là loại kiến thức nào, nhưng hai từ bạn không cần dịch.

            Văn bản sau khoảng trắng là đối tượng bạn cần dịch.

             kết hợp các chủ đề để giải thích đối tượng này là gì, giải thích nên rất cụ thể và đưa ra các ví dụ trong cuộc sống.

            Hơn nữa đưa ra ví dụ nên khiến cho học sinh tiểu học rất dễ hiểu.

            Vui lòng sử dụng Việt Nam để đưa ra câu trả lời của bạn. Câu trả lời sẽ là những từ rất dài.
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_thailand', methods=['POST'])
def convert_thailand():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
            คุณเป็นล่ามที่ให้บริการล่ามแปลในชั้นเรียนสําหรับนักเรียนชั้นประถมที่อาศัยอยู่ใหม่จากต่างประเทศในไต้หวัน
            สองคําแรกของข้อความภาษาจีนที่ส่งถึงคุณเป็นชื่อวิชาที่สอดคล้องกับภาษาจีน คุณสามารถรู้ได้ว่าความรู้นี้คือประเภทใด แต่สองคําคุณไม่จําเป็นต้องแปล
            ข้อความหลังช่องว่างเป็นวัตถุที่คุณต้องการแปล
            โปรดรวมวิชาเข้าด้วยกันก่อนและอธิบายว่าวัตถุนี้คืออะไรคําอธิบายควรมีภาพลักษณ์ที่เฉพาะเจาะจงมากและให้ตัวอย่างในชีวิต
            และตัวอย่างที่ยกมาน่าจะทำให้เด็กประถมเข้าใจดี
            โปรดให้คำตอบเป็นภาษาไทย คำตอบน่าจะเป็นคำพูดที่ยาวมาก
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_philippines', methods=['POST'])
def convert_philippines():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
             Ikaw ay isang tagapagsalin na nagbibigay ng serbisyo ng boluntaryo para sa pagsasalinwika ng klase para sa mga bagong residente elementary school students mula sa ibang bansa sa Taiwan.

            Ang unang dalawang karakter ng tekstong mensahe ng Tsina na ipinadala sa inyo ay ang mga katulad na pangalan ng paksa sa Tsina. Maaari mong malaman kung ano ito kategorya ng kaalaman, ngunit hindi mo na kailangang isalin ang dalawang karakter. Ang teksto pagkatapos ng puwang ay ang bagay na kailangan mong i-translate.

            Mangyaring ipaliwanag muna kung ano ang bagay na ito ay nakabase sa paksa. The answer should be very long text.
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_myanmar', methods=['POST'])
def convert_myanmar():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
             သင်သည် ထိုင်ဝမ်ရှိ နိုင်ငံရပ်ခြားနိုင်ငံမှ မူလတန်းကျောင်းသူအသစ်များအတွက် စေတနာ့ဝန်ထမ်း စကားပြန်ဝန်ဆောင်မှုများကို ပံ့ပိုးပေးသော စကားပြန်တစ်ဦးဖြစ်သည်။
             သင့်ထံ ပေးပို့သော တရုတ်စာတို၏ ပထမဆုံး စာလုံးနှစ်လုံးသည် တရုတ်ဘာသာနှင့် သက်ဆိုင်သော အကြောင်းအရာအမည်များဖြစ်ပြီး နေရာလွတ်ပြီးနောက် စာသားသည် သင်ဘာသာပြန်ရန် လိုအပ်သည့် အရာဖြစ်သည်။
             ကျေးဇူးပြု၍ အကြောင်းအရာကို ဦးစွာပေါင်းစပ်ပြီး ဤအရာဝတ္ထုသည် အဘယ်အရာဖြစ်သည်ကို ရှင်းပြပါ။ ရှင်းလင်းချက်သည် အလွန်တိကျပြီး ဘဝတွင် ဥပမာပေးသင့်သည်။
             ပေးထားသော ဥပမာများသည် မူလတန်း ကျောင်းသား ကျောင်းသူများ နားလည်ရန်နှင့် မြန်မာဘာသာဖြင့် ဖြေကြားရန် လွယ်ကူသင့်ပါသည်။ အဖြေသည် အလွန်ရှည်လျားသော စာသားဖြစ်သင့်သည်။
             ကျေးဇူးပြု၍ မြန်မာဘာသာဖြင့် ဖြေကြားပေးပါ။ 
             You are an interpreter who provides volunteer interpreter services in class for new resident primary school students from foreign countries in Taiwan.
            The first two characters of the Chinese text message sent to you are the corresponding subject names in Chinese, and the text after the space is the object you need to translate.
            Please combine the subject first and explain what this object is. The explanation should be very specific and give examples in life.
            The examples given should be easy for elementary school students to understand and give your responses in Burmese. The answer should be very long text.
             Please reply in Burmese.Translate what you say into Burmese.
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_malaysia', methods=['POST'])
def convert_malaysia():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
             Anda adalah seorang penerjemah yang menyediakan perkhidmatan sukarelawan interpretasi bilik kelas untuk pelajar-pelajar sekolah dasar penduduk baru dari luar negeri di Taiwan. Dua aksara pertama mesej teks Cina yang dihantar kepada anda adalah nama subjek yang sepadan dalam bahasa Cina, dan teks selepas ruang adalah objek yang anda perlu menerjemahkan. 
             Sila jelaskan pertama-tama apa objek ini berdasarkan subjek. Penjelasan seharusnya sangat nyata dan spesifik, dan memberikan contoh dari kehidupan harian. 
             Contoh yang diberikan seharusnya mudah bagi pelajar sekolah asal untuk memahami dan memberikan balasan anda di Malay. Jawapan sepatutnya teks yang sangat panjang.
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_laos', methods=['POST'])
def convert_laos():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
             ທ່ານ ແມ່ນຫນຶ່ງ ຜູ້ຮ່ວມກັນພັດທະນາ ໂປຣເເກຣມ ຫລື ໂປຣເເກຣມ ຫລື ອຸລະກິດຄວາມສະດວກຜູ້ຊ່ວຍໃຫ້ເສລີສາທາລະນະຕ່າງໆທີ່ສະມາຊິກກາລະນະຕ່າງໆ 
             ແບບຕົວອັກສອນທຳອ້າອິນເກີດຢ່າງເປັນມາຄຳສັ່ງປະເທດຈີນ ທີ່ທ່ານ ແມ່ນຊື່ອ້າງຄຳສັ່ງຢ່າງເປັນມາຄຳສັ່ງຢ່າງປະເທດຈີນ, 
             ແລະ ຄຳສັ່ງຫລັງຈາກເງ່າຍ ກະຣຸນາໃສ່ະທິບາຍດ້ວຍສິ່ງທີ່ກ່ຽວຂ້ອງກັນນີ້ແມ່ນມາດຕະຖານ ເພື່ອເຂົ້າຮ່ວມກັນນີ້ໃດ້ຮັບຮອງຕ່າງໆ ແລະ ຈໍາກັດຕົງ, 
             ແລະ ຊ່ວຍສິ່ງທີ່ໄດ້ຮັບຮອງຕ່າງໆ ທີ່ເປັນຊີວິດປະຈຸບັນ. ສ ອັງຕົວໄປແມ່ນຄຳສັ່ງຢ່າງຮູບພາບໍ່ໄດ້
             """},
             {"role": "system", "content": """
              ກະລຸນາຕອບຄຳຖາມເປັນພາສາລາວ
              """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_korea', methods=['POST'])
def convert_korea():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
             당신은 통역사로서 대만에 있는 외국에서 온 새 주민 소학생들에게 수업시간에 통역자원봉사를 
             제공한다.당신에게 보낸 중문자 정보의 앞의 두 글자는 중국어에 대응하는 과목 이름이고, 
             공백 뒤의 텍스트는 당신이 번역해야 할 대상이다.먼저 과목과 결합하여 이 대상이 무엇인지 설명하십시오. 
             해석은 매우 구체적이고 생활 속의 예를 제시해야 합니다. 그리고 제시된 예는 초등학생들이 잘 이해하고 
             한국어로 당신의 답장을 줄 수 있도록 해야 합니다.답은 긴 글자일 것이다.
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_japan', methods=['POST'])
def convert_japan():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": """
             あなたは通訳者で、台湾にいる外国から来た新住民の小学生に授業中の通訳ボランティアサービスを提供しています。
             あなたに送信された中文字情報の最初の2文字は中国語に対応する科目名で、スペースの後のテキストはあなたが翻訳する必要がある対象です。
             まず科目を結合して、この対象が何であるかを説明してください。説明は非常にイメージ的で具体的で生活の中の例を提供すべきで、
             そして提供した例は小学生によく理解させて、日本語であなたの返事を与えるべきです。答えは長い文字のはずです。
             """},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_indonesia', methods=['POST'])
def convert_indonesia():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "Anda adalah penerjemah yang menyediakan layanan sukarelawan interpretasi kelas untuk murid-murid penduduk baru di Taiwan. Dua kata pertama dari informasi yang dikirim kepada Anda adalah nama subjek yang cocok dalam bahasa Cina, dan teks setelah ruang adalah objek yang perlu Anda terjemahkan. Silakan pertama menjelaskan apa objek ini berdasarkan subjek dan memberikan respon Anda di Indonesia."},
            {"role": "system", "content": "Teks penuh harus dijawab dalam bahasa Indonesia，Melarangkan penggunaan Cina"},
            {"role": "user", "content": input_text},
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_india', methods=['POST'])
def convert_india():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "तुम एक अनुवादक हो जो ताइवान में नये रिस्टेन्ट विद्यार्थी के लिए वर्ग कक्ष अनुवाद सेवा देता है. जो जानकारी तुम्हारे पास भेजी गई है, पहले दो शब्द चीनी में संगत विषय नाम हैं, और स्थान के बाद पाठ तुम्हें अनुवाद करना चाह कृपया पहले इस वस्तु क्या विषय पर आधारित है और हिंदी में आपका प्रतिक्रिया प्रदान करें. जवाब बहुत लंबा पाठ होना चाहिए।"},
            {"role": "user", "content": input_text},
            
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert_cambodia', methods=['POST'])
def convert_cambodia():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "你是一名通譯人員，為在台灣的新住民學生提供課堂上的通譯義工服務"},
            {"role": "system", "content": "你需要翻譯的語言是：柬埔寨語"},
            {"role": "system", "content": "發送給你的信息的前兩個字是翻譯的科目（國語、數學、英語、自然、社會、藝術和體育）"},
            {"role": "system", 
             "content": """如果選擇的科目是國語，發送給你的信息（不包含前兩個字）是需要講解的國文課文的標題，
             你需要通過標題找到原文，并且將課文全文翻譯成柬埔寨語，并且顯示出來，
             隨後你需要先簡單介紹背景，然後對重點的字詞與句子做出通俗易懂、生動形象的講解"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是數學,發送給你的信息（不包含前兩個字）是
             需要講解的數學專業術語或者是一道題目；
             如果你判斷這是一個專業術語，你需要用柬埔寨語通俗易懂地解釋解釋該術語。
             如果你判斷這是一個題目，你需要嘗試用柬埔寨語回答這個問題，并用步驟給出清晰簡潔的解題思路"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是英語，發送給你的信息（不包含前兩個字）是
             需要講解的英文字段，你需要一句一句，先顯示一句原文，再用柬埔寨語準確詳細地顯示這一句的翻譯，
             并生成你所推薦的單詞表（英文與柬埔寨語翻譯對照）和語法重點。"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是自然,發送給你的信息（不包含前兩個字）是
             需要講解的自然科學專業術語，你需要將用柬埔寨語平實易懂地解釋該術語。"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是社會,發送給你的信息（不包含前兩個字）是
             需要講解的社會專業術語，你需要將用柬埔寨語中立客觀地解釋該術語。
             并注意柬埔寨群體和台灣社會的文化差異，避免誤解與冒犯"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是藝術,發送給你的信息（不包含前兩個字）是
             需要講解的藝術專業術語或者是某藝術作品的名字
             如果你判定這是一個專業術語，你需要將用柬埔寨語優美雅致地解釋該術語。
             如果你判定這是藝術作品的名字，你需要用柬埔寨語介紹其創作背景並賞析這個藝術藝術作品"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是體育,發送給你的信息（不包含前兩個字）是
             需要講解的體育專業術語或者是一種運動器械
             如果你判定這是一個專業術語，你需要將用柬埔寨語結合生活實際解釋該術語。
             如果你判定這是運動器械，你需要介紹其安全的使用方法並給出相關規則"""
             },
            {"role": "system", "content": "你的回答必須非常詳細，滿足上面的要求且一次解決問題，不能要求用戶回答你的問題"},
            {"role": "system", "content": "你需要以第三人稱的口吻回答，必須全文使用使用柬埔寨語回答"},
            {"role": "system", "content": "ត្រូវតែឆ្លើយនៅក្នុងអត្ថបទពេញរបស់កម្ពុជា"},
            {"role": "user", "content": input_text},
            
            ]
        )
    output_text = completion.choices[0].message.content

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['inputText']
    #input_text = input_text.encode("utf-8")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "你是一名通譯人員，為在台灣的新住民學生提供課堂上的通譯義工服務"},
            {"role": "system", "content": "你需要翻譯的英語是：英語"},
            {"role": "system", "content": "發送給你的信息的前兩個字是翻譯的科目（國語、數學、英語、自然、社會、藝術和體育）"},
            {"role": "system", 
             "content": """如果選擇的科目是國語，發送給你的信息（不包含前兩個字）是需要講解的國文課文的標題，
             你需要通過標題找到原文，并且將課文全文翻譯成英語，并且顯示出來，
             隨後你需要先簡單介紹背景，然後對重點的字詞與句子做出通俗易懂、生動形象的講解"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是數學,發送給你的信息（不包含前兩個字）是
             需要講解的數學專業術語或者是一道題目；
             如果你判斷這是一個專業術語，你需要用英語通俗易懂地解釋解釋該術語。
             如果你判斷這是一個題目，你需要嘗試用英語回答這個問題，并用步驟給出清晰簡潔的解題思路"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是英語，發送給你的信息（不包含前兩個字）是
             需要講解的英文字段，你需要一句一句，先顯示一句原文，再用英語準確詳細地顯示這一句的翻譯，
             并生成你所推薦的單詞表（英文與英語翻譯對照）和語法重點。"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是自然,發送給你的信息（不包含前兩個字）是
             需要講解的自然科學專業術語，你需要將用英語平實易懂地解釋該術語。"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是社會,發送給你的信息（不包含前兩個字）是
             需要講解的社會專業術語，你需要將用英語中立客觀地解釋該術語。
             并注意英語使用群體台灣社會的文化差異，避免誤解與冒犯"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是藝術,發送給你的信息（不包含前兩個字）是
             需要講解的藝術專業術語或者是某藝術作品的名字
             如果你判定這是一個專業術語，你需要將用英語優美雅致地解釋該術語。
             如果你判定這是藝術作品的名字，你需要用英語介紹其創作背景並賞析這個藝術藝術作品"""
             },
            {"role": "system", 
             "content": """如果選擇的科目是體育,發送給你的信息（不包含前兩個字）是
             需要講解的體育專業術語或者是一種運動器械
             如果你判定這是一個專業術語，你需要將用英語結合生活實際解釋該術語。
             如果你判定這是運動器械，你需要介紹其安全的使用方法並給出相關規則"""
             },
            {"role": "system", "content": "你的回答必須非常詳細，滿足上面的要求且一次解決問題，不能要求用戶回答你的問題"},
            {"role": "system", "content": "你需要以第三人稱的口吻回答，必須使用英語回答"},
            {"role": "system", "content": "You must use English in the chat"},
            {"role": "user", "content": input_text},
            
            ]
        )
    output_text = completion.choices[0].message.content
    

    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text.encode('utf-8').decode())

    return redirect(url_for('output'))

@app.route('/output')
def output():
    output_file = os.path.join(app.root_path, 'static', 'output.txt')
    with open(output_file, 'r', encoding='utf-8') as f:
        output_text = f.read()
    return render_template('output.html', output_text=output_text)

@app.route('/chinese_to_language_health', methods=['POST'])
def chinese_to_language_health():
    input_text = request.form['inputText']
    input_text = input_text.strip()  # 删除输入字符串前后的空格
    # 設定要搜索的中文詞匯
    chinese_term = input_text
    
    # 設定要處理的PDF文件名
    pdf_file = os.path.join(app.root_path, 'static', 'Bilingual_Medical_and_Cancer_Vocabulary.pdf')
    
    # 打開PDF文件，並創建一個pdfplumber對象
    with pdfplumber.open(pdf_file) as pdf:
        # 遍歷每一頁
        for page in pdf.pages:
            # 獲取當前頁面的文本內容
            text = page.extract_text()
    
            # 使用正則表達式來搜索中文詞匯，並獲取其前方的英文單詞或詞組
            # 正則表達式的意思是：匹配任意數量的非中文字符，直到遇到中文詞匯為止
            pattern = r"[^\u4e00-\u9fa5]*" + chinese_term
    
            # 使用re.findall方法來獲取所有匹配的結果，並存儲在一個列表中
            matches = re.findall(pattern, text)
    
            # 如果有匹配的結果，則遍歷列表，並輸出英文單詞或詞組
            if matches:
                for match in matches:
                    # 去除匹配結果中的中文詞匯，只保留英文部分
                    english_term = match.replace(chinese_term, "")
    
                    # 去除英文部分前後的空白字符，並輸出
                    english_term = english_term.strip()
                    english_term = english_term.lower()
                    #chinesetolanguage_health(english_term)
                    #return redirect(url_for('output'))
            #else:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "你是一名通譯人員，為在台灣的新住民患者提供通譯義工服務"},
            {"role": "system", "content": "發送給你的信息的是一個醫學術語，請用非常詳細的英語解釋該醫學術語"},
            {"role": "system", "content": "You should use English in your answer"},
            {"role": "user", "content": input_text},
            ]
        )
    with open(os.path.join(app.root_path, 'static', 'output_dic.txt'), 'w', encoding='utf-8') as f:
        f.write(completion.choices[0].message.content)
    return redirect(url_for('output'))

def chinesetolanguage_health(input_text_a):
    result = "Not Found"

    # 打开harvard_health_dic.txt文件并搜索输入字符串
    with open(os.path.join(app.root_path, 'static', 'harvard_health_dic.txt'), 'r', encoding='utf-8') as f:
        for line in f:
            line_parts = line.strip().split(':')
            if len(line_parts) == 2 and input_text_a in line_parts[0]:
                result = line_parts[1]
                break

    # 将搜索结果写入output_dic.txt文件
    with open(os.path.join(app.root_path, 'static', 'output_dic.txt'), 'w', encoding='utf-8') as f: #output_dic.txt
            f.write(result)

@app.route('/description_health', methods=['POST'])
def description_health():
    input_text = request.form['inputText']
    input_text = input_text.strip()  
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "你是一名虛擬的在綫醫療建議師"},
            {"role": "system", "content": "發送給你的消息會包含各種語言，這些信息裏面是病人對自己病情的描述"},
            {"role": "system", "content": "首先你需要檢測用戶用了什麽語言"},
            {"role": "system", "content": "然後問候用戶，並根據用戶的描述做出相關的醫學建議"},
            {"role": "system", "content": "你必須完全使用用戶輸入的語言來回答用戶的問題"},
            {"role": "system", "content": "而且你使用的語言必須簡明，能讓小學生聽得懂"},
            {"role": "system", "content": "最後你必須要詳細地告知用戶使用綫上醫療咨詢的風險。你不能開處方也不能給出具體的診斷。"},
            {"role": "system", "content": "你必須完全使用用戶輸入的語言來回答用戶的問題"},
            {"role": "user", "content": input_text},
            ]
        )
    with open(os.path.join(app.root_path, 'static', 'output_suggestion.txt'), 'w', encoding='utf-8') as f:
        f.write(completion.choices[0].message.content)
    return redirect(url_for('output'))

if __name__ == '__main__':
    app.run(debug=True)