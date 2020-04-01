from datetime import *

def age(date1,date2):
    """
    Returns the number of whole years between 
    the given dates
    """
    delta=date1-date2
    years=delta.days/365.24
    years=int(years)
    return years


