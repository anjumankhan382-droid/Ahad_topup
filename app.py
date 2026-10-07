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
        from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

BKASH_NUMBER = "01727246581"
TELEGRAM_BOT_TOKEN = "8970671481:AAFACF5V3b59JyLbdBNzszEH5VAlyefhLww"
TELEGRAM_CHAT_ID = "8662169982"

def send_telegram_notification(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print("Error:", e)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ahad TopUp - Premium Free Fire Shop</title>
    <style>
        body { font-family: sans-serif; background-color: #0b0f19; color: #fff; margin: 0; padding: 20px; text-align: center; }
        .container { max-width: 400px; margin: auto; background: #1e293b; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        input, select { width: 100%; padding: 10px; margin: 8px 0; border-radius: 6px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box; }
        button { background: #f59e0b; color: #000; font-weight: bold; padding: 12px; width: 100%; border: none; border-radius: 6px; cursor: pointer; margin-top: 10px; }
        .bkash { background: #db2777; padding: 10px; border-radius: 6px; margin: 10px 0; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🔥 Ahad TopUp 🔥</h2>
        <p style="color:#38bdf8;">100% Trusted Free Fire Store</p>
        
        {% if not success %}
        <form method="POST">
            <input type="email" name="email" required placeholder="আপনার জিমেইল আইডি">
            <input type="text" name="uid" required placeholder="ফ্রি ফায়ার UID">
            
            <select name="package" required>
                <option value="25 Dias - 25 BDT">২৫ ডায়মন্ড - ২৫ টাকা</option>
                <option value="115 Dias - 85 BDT">১১৫ ডায়মন্ড - ৮৫ টাকা</option>
                <option value="Weekly - 160 BDT">সাপ্তাহিক মেম্বারশিপ - ১৬০ টাকা</option>
                <option value="Monthly - 450 BDT">মাসিক মেম্বারশিপ - ৪৫০ টাকা</option>
            </select>

            <div class="bkash">
                বিকাশ পার্সোনাল: {{ bkash }}<br>
                <small>প্রথমে এই নম্বরে টাকা পাঠান</small>
            </div>

            <input type="text" name="sender" required placeholder="যে বিকাশ নম্বর থেকে পাঠিয়েছেন">
            <input type="text" name="trx" required placeholder="ট্রানজাকশন আইডি (TrxID)">

            <button type="submit">অর্ডার কনফার্ম করুন</button>
        </form>
        {% else %}
            <h3 style="color: #4ade80;">🎉 অর্ডার সফল হয়েছে!</h3>
            <p>আপনার পেমেন্ট চেক করে দ্রুত ডায়মন্ড দেওয়া হবে।</p>
            <a href="/" style="color:#f59e0b; text-decoration:none;">আরেকটি অর্ডার করুন</a>
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
        
        msg = f"🚨 *নতুন অর্ডার!* 🚨\n📧 Gmail: `{email}`\n🎮 UID: `{uid}`\n📦 Package: `{package}`\n📱 Sender: `{sender}`\n🔑 TrxID: `{trx}`"
        send_telegram_notification(msg)
        success = True
        
    return render_template_string(HTML_TEMPLATE, bkash=BKASH_NUMBER, success=success)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
