from datetime import datetime as dt


def academic_yr():
    current_yr = dt.now().year
    previous_yr = current_yr - 1
    academic_year = str(previous_yr)+'/'+str(current_yr)
    return academic_year
