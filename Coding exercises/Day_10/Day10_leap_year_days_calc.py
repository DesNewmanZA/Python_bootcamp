# Function to determine if the year is a leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Function that determines the number of days in the month based on if
# the year is a leap year
def days_in_month(year, month):
  # Define list of number of days in a month
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

  # Determine if the year is a leap year
  leap_year = is_leap(year)

  # If it's a leap year and the month is Feb, we return 29
  # Else we just check the list of number of days in a month and return it
  if leap_year and month == 2:
    return 29
  else:
    return month_days[month - 1]

# Call functions
year = int(input()) 
month = int(input()) 
days = days_in_month(year, month)
print(days)

