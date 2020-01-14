from content import mail
from flask_mail import Message
from datetime import datetime as dt


def sendEmail(_name, _subject, _email, _message):
    # SEND EMAIL
    _recipient = 'agmschool.management@gmail.com'
    msg = Message(_subject, sender=('AGMS Contact', 'isolveitgroup@gmail.com'), recipients=[_recipient])
    assert msg.sender == "AGMS Contact <isolveitgroup@gmail.com>"
    msg.body = f'''{_message}

Sender's Name: {_name}
Sender's Email: {_email}
Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(msg)
    return 'Sent'


def replyMessage(_email, _sender):
    # REPLY EMAIL
    _subj = 'Message Received'
    mesg = Message(_subj, sender=('AGMS Contact', 'isolveitgroup@gmail.com'), recipients=[_email])
    assert mesg.sender == "AGMS Contact <isolveitgroup@gmail.com>"
    mesg.body = f'''Hello {_sender},
The message sent by {_sender} to AGMS Contact has been received. AGMS Contact will contact you within 24 hours.

Thank you,
AGMS Contact.

Date Sent:  {dt.now().strftime('%B %d, %Y, %H:%M ') + 'GMT'}
'''
    mail.send(mesg)
    return 'OK'