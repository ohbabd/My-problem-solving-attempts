# This script calculates how many days are there between two given dates                                    
# Dates are supposed to be correct                                                                               
                                                                                                           
                                                                                                           
monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   # Array to store days of months            
                                                                                                           
                                                                                                           
def leap_year(year1, year2):                    # calculates how many leap years                           
    leap = 0                                    # there are between the two dates.                         
    while year1 <= year2:                                                                                  
        if year1 % 4 == 0:                                                                                 
            leap = leap + 1                                                                                
            if year1 % 100 == 0 and year1 % 400 != 0:                                                      
                leap = leap - 1                                                                            
        year1 = year1 + 1                                                                                  
    return leap                                                                                            
                                                                                                           
                                                                                                           
def add_or_sub_days(month, day):                # Calculates the number of days we should                  
    i = 0                                       # include/exclude after the second/first year              
    days = 0                                                                                               
    while i + 1 < month:                                                                                   
        days = days + monthsDays[i]                                                                        
        i = i + 1                                                                                          
    return days + day - 1                                                                                  
                                                                                                           
                                                                                                           
def days_between_dates(year1, month1, day1, year2, month2, day2):                                          
    days_between_years = (year2 - year1) * 365 + leap_year(year1, year2)  # total days between the 2 years 
    days2sub = add_or_sub_days(month1, day1)  # days to exclude after the first year                       
    days2add = add_or_sub_days(month2, day2)  # days to include after the second year                      
    days = days_between_years + days2add - days2sub                                                        
                                                                                                           
    if year1 % 100 == 0 and year1 % 400 != 0:  # Checks if year2 is a leap year                            
        leap = False                                                                                       
    elif year1 % 4 == 0:                                                                                   
        leap = True                                                                                        
                                                                                                           
    if month2 <= 2 and leap:                 # Also if the second date is before February 29th             
        days = days - 1                      # in a leap year we should not add a leap day.                
        if day2 == 29:                       # And if the second date is exactly February 29th in          
            days = days - 1                  # a leap year, we will add 2 leap days, so we subtract 1 here.
                                                                                                           
    return days                                                                                            
