from flask import render_template, redirect, request, url_for, flash, Markup, jsonify
from content import app, mongo
from datetime import datetime as dt
from .contact import sendEmail, replyMessage
from .py_files.academic_yr import academicYr
from .py_files.form import ContactForm


'''/=========ROUTES===========/'''


# HOME PAGE
@app.route('/')
@app.route('/home')
def index():
    _year = dt.now().strftime('%Y')
    return render_template('index.html', _year=_year)


# OUR SCHOOL PAGE
@app.route('/about')
def about():
    _year = dt.now().strftime('%Y')
    return render_template('about.html', _year=_year)


# ADMISSION PAGE
@app.route('/admission')
def admission():
    _year = dt.now().strftime('%Y')
    return render_template('admission.html', _year=_year)


# 1.Admission Forms page
@app.route('/admission/forms', methods=['GET', 'POST'])
def admission_forms():
    otp = request.args.get('OTP_input', type=str)
    query = mongo.db.admission_form_OTP
    data = query.find_one({'OTP': otp})
    if data is None:
        output = "OTP is invalid, try again."
        return jsonify(result=output, status=404)
    elif data['used'] == 1:
        output = "OTP has been used."
        return jsonify(result=output, status=404)
    else:
        query.update_one(
            {'OTP': data['OTP']},
            {'$set': {"used": 1, "date_used": dt.now()}}
        )
        output = 'https://forms.gle/aYAxiNCxcEwUYQyN6'
        return jsonify(result=output, status=200)


# GALLERY PAGE
# 1.Future Career page
@app.route('/gallery/future_career')
def future():
    _year = dt.now().strftime('%Y')
    return render_template('future.html',  _year=_year)


# 2.Culture Awareness page
@app.route('/gallery/culture_awareness')
def culture():
    _year = dt.now().strftime('%Y')
    return render_template('culture.html',  _year=_year)


# 3.School's Album page
@app.route('/gallery/sch_album')
def schAlbum():
    _year = dt.now().strftime('%Y')
    return render_template('schalbum.html', _year=_year)


# 2.Calendar page
@app.route('/academics/calendar')
def calendar():
    _year = dt.now().strftime('%Y')
    return render_template('calendar.html', _year=_year, academic=academicYr())


# CONTACT PAGE
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    _year = dt.now().strftime('%Y')
    form = ContactForm(request.form)
    if request.method == 'POST':
        _name = form.name.data
        _email = form.e_mail.data
        _subject = form.subject.data
        _message = form.message.data
        
        replyMessage(_email, _name)
        _mailSent = sendEmail(_name, _subject, _email, _message)

        if _mailSent == 'Sent':
            flash('Message sent successfully.', 'success')
            return redirect(url_for('contact'))
        else:
            error = Markup("Error Sending Message")
            return render_template('contact.html', error=error, form=form)
    return render_template('contact.html', _year=_year, form=form)





