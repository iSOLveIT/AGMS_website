from datetime import datetime as dt

def academicYr():
    current_yr = dt.now().year
    previous_yr = current_yr - 1
    academic_year = str(previous_yr)+'/'+str(current_yr)
    return academic_year

'''def deleteFile():
    current_yr = dt.now().year
    previous_yr = current_yr - 1
    later_yr = current_yr - 2
    prev_academic_year = str(later_yr)+'/'+str(previous_yr)
    return prev_academic_year'''