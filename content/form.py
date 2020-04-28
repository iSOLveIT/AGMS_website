from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
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
        validators.Length(max=250)
    ])

