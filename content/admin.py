from flask import render_template
from content import app
from datetime import datetime as dt


"""ERROR HANDLERS"""
# ERRORS PAGE
# 1.Error_404 Page
@app.errorhandler(404)
def error_404(error):
    _year = dt.now().strftime('%Y')
    _error = '404'
    return render_template('error_404.html', _year=_year, _error=_error), 404

# 2.Error_500 page
@app.errorhandler(500)
def error_500(error):
    _year = dt.now().strftime('%Y')
    _error = '500'
    return render_template('error_500.html', _year=_year, _error=_error), 500


