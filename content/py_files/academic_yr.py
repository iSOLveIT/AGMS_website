from datetime import datetime as dt
import random
from content import mongo


def academicYr():
    current_yr = dt.now().year
    previous_yr = current_yr - 1
    academic_year = str(previous_yr)+'/'+str(current_yr)
    return academic_year


def numGenerator():
    s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_list = random.sample(s, 7)
    output = ''.join(random_list)
    query = mongo.db.admission_form_OTP
    result = query.find_one({'OTP': output})
    if result is not None:
        numGenerator()
    if result is None:
        query.insert_one({'OTP': output, 'used': 0, 'date_created': dt.now(), 'date_used': dt.now()})
        return output

#print(numGenerator())