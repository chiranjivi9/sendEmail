import smtplib
from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME']='@gmail.com'
app.config['MAIL_PASSWORD']= ''

mail = Mail(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    # try:
        msg = Message("THIS IS A PYTHON TEST",
                  sender="@gmail.com",
                  recipients=["@gmail.com"],
                  body='Email sent via flask app by CJ',
                  html= render_template('result.html'))

        mail.send(msg)

        return 'SUCCESS : EMAIL SENT'

    # except Exception as e:
        # return str(e)

if __name__ == '__main__':
    app.run(debug=True)
