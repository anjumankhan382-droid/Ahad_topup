from flask import Flask, render_template_string, request

app = Flask(__name__)
BKASH_NUMBER = "01727246581"

HTML = """
<!DOCTYPE html>
<html>
<head><title>Ahad TopUp</title></head>
<body style="background:#0f172a; color:white; text-align:center; padding:50px; font-family:sans-serif;">
    <h2>🔥 Ahad TopUp 🔥</h2>
    <p>বিকাশ পার্সোনাল: <b>{{ bkash }}</b></p>
    {% if not done %}
    <form method="POST">
        <p>UID: <input type="text" name="uid" required></p>
        <p>প্যাকেজ: <select name="pkg"><option>২৫ ডায়মন্ড - ২৫ টাকা</option><option>১১৫ ডায়মন্ড - ৮৫ টাকা</option></select></p>
        <p>বিকাশ নম্বর: <input type="text" name="sender" required></p>
        <p>TrxID: <input type="text" name="trx" required></p>
        <button type="submit">কনফার্ম করুন</button>
    </form>
    {% else %}
        <h3 style="color:#4ade80;">অর্ডার সফলভাবে জমা হয়েছে!</h3>
        <a href="/">আরেকটি অর্ডার করুন</a>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    done = False
    if request.method == 'POST':
        print(f"Order: UID={request.form.get('uid')}, Trx={request.form.get('trx')}")
        done = True
    return render_template_string(HTML, bkash=BKASH_NUMBER, done=done)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
