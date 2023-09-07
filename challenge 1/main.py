#leap year 

'''
year % 4== $
year % 100 != 0/
year % 400 == 0

'''
def isLeapYear(year ):
     if(year% 4 == 0 and  year % 100 != 0):
         return True 
     else:
         return False

year = 2012

if isLeapYear(year):
  print("{} is a leapyear".format(year))
else:
   print("{} is not a leapyear".format(year))