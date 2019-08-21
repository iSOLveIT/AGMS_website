from content import mail
from flask_mail import Message
from datetime import datetime as dt



"""FUNCTION FOR SENDING EMAIL"""
def sendEmail(_name, _subject, _email, _message):
    # SEND EMAIL
    _recipient = 'agmschool.management@gmail.com'
    msg = Message(_subject, sender=('AGMS Contact Page', 'agmschool.management@gmail.com'), recipients=[_recipient])
    assert msg.sender == "AGMS Contact Page <agmschool.management@gmail.com>"
    msg.body = f'''{_message}


Sender's Name: {_name}
Sender's Email: {_email}
Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(msg)
    return 'Sent'