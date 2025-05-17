from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

APP_ID = 'your_app_id'
APP_SECRET = 'your_app_secret'

@app.route('/zalo/callback')
def zalo_callback():
    code = request.args.get('code')
    if not code:
        return "Missing code", 400

    # Gọi API để lấy access_token
    token_url = 'https://oauth.zaloapp.com/v4/access_token'
    params = {
        'app_id': APP_ID,
        'app_secret': APP_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }

    response = requests.get(token_url, params=params)
    data = response.json()

    if 'access_token' in data:
        access_token = data['access_token']
        # TODO: Lưu access_token vào DB hoặc nơi bạn cần
        return jsonify({"access_token": access_token, "message": "Lấy token thành công"})
    else:
        return jsonify({"error": data}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
