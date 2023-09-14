import smtplib #smtp = it is server for email
from email.message import EmailMessage

email = EmailMessage()
email['from']='bee'
email['to']='pythonexo@gmail.com'
email['subject']='exo'

email.set_content('i am a student')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: 
    smtp.ehlo()     # msg
    smtp.starttls() #connect securely to the server
    smtp.login('pythonexo@gmail.com','zsrlejzmunoaaxqt')
    smtp.send_message(email)
    print('all good')
    
# Desktop\Python_w_Udemy\Section17_Scripting with Python\Email> python msg.py
# all good



