import smtplib #smtp = it is server for email
from email.message import EmailMessage
from string import Template
from pathlib import Path # it gives access to the html file

# we have a db of all the emails so want to customize the email for each specific pers.

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from']='bee'
email['to']='pythonexo@gmail.com'
email['subject']='exo'

email.set_content(html.substitute({'name':'fas'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: 
    smtp.ehlo()     # msg
    smtp.starttls() #connect securely to the server
    smtp.login('pythonexo@gmail.com','zsrlejzmunoaaxqt')
    smtp.send_message(email)
    print('all good')
    