from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

orders = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Fire Top-up BD</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0f172a; color: #fff; margin: 0; padding: 20px; }
        .container { max-width: 400px; margin: auto; background: #1e293b; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
        h2 { text-align: center; color: #38bdf8; }
        .payment-notice { background: #334155; padding: 10px; border-radius: 5px; margin-bottom: 15px; border-left: 4px solid #f43f5e; }
        input, select { width: 100%; padding: 10px; margin: 10px 0; background: #334155; border: 1px solid #475569; color: #fff; border-radius: 5px; }
        button { width: 100%; padding: 10px; background: #2563eb; border: none; color: white; font-weight: bold; border-radius: 5px; cursor: pointer; }
        button:hover { background: #1d4ed8; }
        .order-box { background: #334155; padding: 10px; margin-top: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🔥 Free Fire Top-up 🔥</h2>
        
        <div class="payment-notice">
            <p style="margin: 0; font-size: 14px;"><b>পেমেন্ট নিয়ম:</b> প্রথমে নিচের নাম্বারে টাকা Send Money করুন এবং ট্রানজাকশন আইডি দিন।</p>
            <p style="margin: 5px 0 0 0; color: #38bdf8; font-weight: bold;">বিকাশ (Personal): 01727246581</p>
        </div>

        <form method="POST" action="/order">
            <label>আপনার জিমেইল:</label>
            <input type="email" name="email" placeholder="example@gmail.com" required>
            
            <label>ফ্রি ফায়ার UID:</label>
            <input type="text" name="uid" placeholder="যেমন: 123456789" required>
            
            <label>প্যাকেজ সিলেক্ট করুন:</label>
            <select name="package">
                <option value="115 Diamonds - 85 BDT">১১৫ ডায়মন্ড - ৮৫ টাকা</option>
                <option value="240 Diamonds - 170 BDT">২৪০ ডায়মন্ড - ১৭০ টাকা</option>
                <option value="610 Diamonds - 450 BDT">৬১০ ডায়মন্ড - ৪৫০ টাকা</option>
            </select>
            
            <label>বিকাশ ট্রানজাকশন আইডি (TrxID):</label>
            <input type="text" name="trxid" placeholder="যেমন: 9N7K..." required>
            
            <button type="submit">অর্ডার কনফার্ম করুন</button>
        </form>
        
        <hr style="border-color: #475569; margin: 20px 0
