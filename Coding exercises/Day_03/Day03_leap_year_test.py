# Take in a year as input and convert to an integer - assume a numeric input was given
year = int(input())

# Years divisible by 4 are leap years, unless they are also divisible by 100 in which case they aren't.
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")