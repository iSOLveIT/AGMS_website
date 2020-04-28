from datetime import datetime as dt
# import random
# from content import mongo


def academic_yr():
    current_yr = dt.now().year
    previous_yr = current_yr - 1
    academic_year = str(previous_yr)+'/'+str(current_yr)
    return academic_year

#
# def random_string():
#     """Generate a random string of letters and digits """
#     s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # Generating a Random String including letters and digits"
#
#     otp = ''.join(random.sample(s, 7))
#     query = mongo.db.admission_form_OTP
#     search = query.find_one({'OTP': otp})
#
#     if search is not None:
#         return random_string()
#     return otp
#
#
# def dbm(generated_string):
#     query = mongo.db.admission_form_OTP
#     query.insert_one({'OTP': generated_string,
#                    'used': 0,
#                    'dateUsed': dt.now()})
#     return None
