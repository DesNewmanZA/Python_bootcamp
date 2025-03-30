# Perform FizzBuzz for numbers 1 to 100
for num in range(1, 101):
  # If divisible by 3 and 5, output FizzBuzz
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  # If only divisible by 3, output Fizz
  elif num % 3 == 0:
    print("Fizz")
  # If only divisible by 5, output Buzz
  elif num % 5 == 0:
    print("Buzz")
  # If all the above fail, output the number
  else:
    print(num)