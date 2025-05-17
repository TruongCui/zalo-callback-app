from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Zalo Callback Server is running."

@app.route('/zalo_callback')
def zalo_callback():
    code = request.args.get('code')
    if code:
        return f"✅ Received code: {code}"
    return "❌ No code received"
