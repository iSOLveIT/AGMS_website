from wtforms import Form, validators, StringField, TextAreaField
from wtforms.fields.html5 import EmailField

class ContactForm(Form):
    name = StringField(validators=[
        validators.DataRequired(),
        validators.InputRequired(),
        validators.Length(max=30)
    ])

    e_mail = EmailField(validators=[
        validators.DataRequired(),
        validators.InputRequired(),
        validators.Length(max=200)
    ])

    subject = StringField(validators=[
        validators.DataRequired(),
        validators.InputRequired(),
        validators.Length(max=20)
    ])

    message = TextAreaField(validators=[
        validators.DataRequired(),
        validators.InputRequired(),
        validators.Length(max=350)
    ])

