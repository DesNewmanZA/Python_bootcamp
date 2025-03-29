# Import needed module
import time

# Define decorator that calculates speed
def speed_calc_decorator(my_funct):
    def wrapper():
      start_time = time.time()
      result = my_funct()
      end_time = time.time()
      print(f"{my_funct.__name__} run time: {end_time - start_time}s")
      return result
    return wrapper

# Define the functions with the decorator
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

# Call the fast and slow functions with the decorator
fast_function()
slow_function()
