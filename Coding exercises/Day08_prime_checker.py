# Function to check if a number is prime
def prime_checker(number):
  # Set a boolean as True - if a divisor is found, set to False
  is_prime = True
  # Search only from the numbers 2 to half of the number for efficiency
  for i in range(2, int(number/2)+1):
    # If divisible, set boolean to false
    if number % i == 0:
      is_prime = False

  # Output is based on the value of the boolean
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input()) 
prime_checker(number=n)