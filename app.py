from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# কনফিগারেশন
BKASH_NUMBER = "01727246581"
TELEGRAM_BOT_TOKEN = "8970671481:AAFACF5V3b59JyLbdBNzszEH5VAlyefhLww"
TELEGRAM_CHAT_ID = "8662169982"

def send_telegram_notification(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print("Telegram Error:", e)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ahad TopUp - Premium Free Fire Shop</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0b0f19; color: #fff; margin: 0; padding: 0; }
        header { background: linear-gradient(135deg, #1e1b4b, #312e81); padding: 20px; text-align: center; border-bottom: 3px solid #f59e0b; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { margin: 0; color: #f59e0b; font-size: 28px; text-transform: uppercase; letter-spacing: 2px; }
        p { color: #94a3b8; }
        .container { max-width: 480px; margin: 20px auto; background: #1e293b; padding: 25px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.6); border: 1px solid #334155; }
        .banner-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 20px; }
        .banner-card { background: #334155; border-radius: 10px; overflow: hidden; text-align: center; border: 2px solid transparent; }
        .banner-card img { width: 100%; height: 100px; object-fit: cover; }
        .banner-card span { display: block; padding: 8px; font-size: 13px; font-weight: bold; color: #facc15; }
        input, select { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box; }
        button { background: linear-gradient(135deg, #f59e0b, #d97706); color: #000; font-weight: bold; padding: 14px; width: 100%; border: none; border-radius: 8px; cursor: pointer; margin-top: 15px; font-size: 16px; transition: 0.3s; box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3); }
        button:hover { background: linear-gradient(135deg, #d97706, #b45309); transform: translateY(-2px); }
        .bkash-box { background: #db2777; color: white; padding: 12px; border-radius: 8px; margin: 15px 0; font-weight: bold; text-align: center; }
        .section-title { color: #38bdf8; border-bottom: 2px solid #334155; padding-bottom: 5px; margin-top: 20px; font-size: 18px; }
    </style>
</head>
<body>
    <header>
        <h1>🔥 Ahad TopUp 🔥</h1>
        <p>100% Trusted Free Fire Diamond Store</p>
    </header>

    <div class="container">
        <div class="banner-grid">
            <div class="banner-card">
                <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=300" alt="Weekly">
                <span>সাপ্তাহিক মেম্বারশিপ</span>
            </div>
            <div class="banner-card">
                <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=300" alt="Monthly">
                <span>মাসিক মেম্বারশিপ</span>
            </div>
        </div>

        {% if not success %}
        <form method="POST">
            <div class="section-title">১. আপনার একাউন্ট ইনফো</div>
            <label style="font-size:13px; color:#cbd5e1;">আপনার জিমেইল আইডি:</label>
            <input type="email" name="email" required placeholder="example@gmail.com">

            <label style="font-size:13px; color:#cbd5e1;">ফ্রি ফায়ার ইউআইডি (UID):</label>
            <input type="text" name="uid" required placeholder="আপনার গেম UID দিন">

            <div class="section-title">২. প্যাকেজ সিলেক্ট করুন</div>
            <select name="package" required>
                <option value="25 Dias - 25 BDT">২৫ ডায়মন্ড - ২৫ টাকা</option>
                <option value="115 Dias - 85 BDT">১১৫ ডায়মন্ড - ৮৫ টাকা</option>
                <option value="Weekly Membership - 160 BDT">সাপ্তাহিক মেম্বারশিপ - ১৬০ টাকা</option>
                <option value="Monthly Membership - 450 BDT">মাসিক মেম্বারশিপ - ৪৫০ টাকা</option>
            </select>

            <div class="bkash-box">
                বিকাশ পার্সোনাল নম্বর:<br>{{ bkash }}<br>
                <small style="font-size:11px;">প্রথমে এই নম্বরে টাকা সেন্ড করুন</small>
            </div>

            <div class="section-title">৩. পেমেন্ট ভেরিফিকেশন</div>
            <label style="font-size:13px; color:#cbd5e1;">বিকাশ নম্বর (যেখান থেকে পাঠিয়েছেন):</label>
            <input type="text" name="sender" required placeholder="01XXXXXXXXX">

            <label style="font-size:13px; color:#cbd5e1;">ট্রানজাকশন আইডি (TrxID):</label>
            <input type="text" name="trx" required placeholder="যেমন: 9H76K54M">

            <button type="submit">অর্ডার কনফার্ম করুন</button>
        </form>
        {% else %}
            <div style="text-align: center; padding: 20px;">
                <h3 style="color: #4ade80; font-size: 22px;">🎉 অর্ডার সফলভাবে জমা হয়েছে!</h3>
                <p>আপনার পেমেন্ট চেক করে দ্রুত ডায়মন্ড পাঠিয়ে দেওয়া হবে।</p>
                <a href="/"><button style="background:#334155; color:#fff;">আরেকটি অর্ডার করুন</button></a>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    success = False
    if request.method == 'POST':
        email = request.form.get('email')
        uid = request.form.get('uid')
        package = request.form.get('package')
        sender = request.form.get('sender')
        trx = request.form.get('trx')
        
        msg = f"🚨 *নতুন অর্ডার এসেছে!* 🚨\n\n📧 *Gmail:* `{email}`\n🎮 *UID:* `{uid}`\n📦 *Package:* `{package}`\n📱 *Sender:* `{sender}`\n🔑 *TrxID:* `{trx}`"
        send_telegram_notification(msg)
        
        success = True
        
    return render_template_string(HTML_TEMPLATE, bkash=BKASH_NUMBER, success=success)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
