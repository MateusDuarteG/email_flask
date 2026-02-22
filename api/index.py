from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurações de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

# Endpoint para enviar e-mail
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    if not data or "to" not in data or "subject" not in data or "body" not in data:
        return jsonify({"error": "Campos obrigatórios: to, subject, body"}), 400
    
    try:
        msg = Message(
            subject=data["subject"],
            recipients=[data["to"]],
            body=data["body"]
        )
        mail.send(msg)
        return jsonify({"message": f"E-mail enviado para {data['to']} com sucesso!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
