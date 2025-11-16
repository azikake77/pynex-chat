# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, send

print("[*] Сервер 'Pynex Chat' запускается...")

app = Flask(__name__)
# Этот 'secret_key' нужен для Flask, может быть любым
app.config['SECRET_KEY'] = 'mysecret_pynex_chat_key!'

# Подключаем SocketIO к нашему Flask-приложению
socketio = SocketIO(app)


@app.route('/')
def index():
    """Эта функция отдает нашу HTML-страницу, когда кто-то заходит на сайт."""
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    """
    Эта функция срабатывает, когда любой клиент (браузер)
    присылает на сервер событие 'message'.
    """
    print(f"[*] Получено сообщение: {msg}")

    # 'broadcast=True' означает "отправить это сообщение всем,
    # кто подключен к чату"
    send(msg, broadcast=True)


if __name__ == '__main__':
    # ВНИМАНИЕ: host='0.0.0.0' ОБЯЗАТЕЛЕН, чтобы к серверу
    # можно было подключиться с других устройств (телефона) в той же сети.
    print("[*] Сервер запущен. Откройте http://ВАШ_IP_АДРЕС:5000 в браузере.")
    socketio.run(app, host='0.0.0.0', port=5000)