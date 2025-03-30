# Create decorator that says what was called and the result
def logging_decorator(fx):
    def wrapper(*args):
        print(f"You called {fx.__name__}{args}")
        result = fx(*args)
        print(f"It returned: {str(result)}")
        return result
    return wrapper


# Main function that sums arguments
@logging_decorator
def a_function(*args):
    return sum(args)
    
# Call function
a_function(1,2,3)