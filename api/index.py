from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Configurações de e-mail usando variáveis de ambiente
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

# Configuração do servidor de e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

if __name__ == "__main__":
    app.run(debug=True)
