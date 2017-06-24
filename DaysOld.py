#This script calculates how many days are there between to given dates
#Dates are supposed correct

# calculates how many leap years
#there are between the two dates.
def leapYear(year1,year2):
    leap = 0
    while year1 <= year2:
        if year1 % 4 == 0:
            leap = leap + 1
            if year1 % 100 == 0 and year1 % 400 != 0:
                leap = leap - 1
        year1 = year1 + 1
    return leap

#Array to store month days
monthsDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# calculates how many days we must not include before
#the first date and after the second date
def daysLived(month,day):
    i = 1
    livedDays = 0
    while i < month:
        livedDays = livedDays + monthsDays[i]
        i = i + 1
    return livedDays + day - 1

#Calculates das between to given dates
def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    days = (year2 - year1) * 365 + leapYear(year1,year2) #Total days between the 2 years
    days2sub = daysLived(month1,day1)                    #Days to exlude
    days = days + days2add - days2sub
    
    if month2 == 2:             # If it's a leap year and month2 is February, we
        days = days - 1         #will add 2 leap days instead of one, so here we
                                #substract 1 day if it's the case
    return days














