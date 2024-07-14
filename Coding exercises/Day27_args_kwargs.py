# Example of *args
def add(*args):
    sum = 0
    for n in args:
        sum += int(n)
    return sum
    
print(add(1,2,3,4))

# Example of **kwargs
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

print(calculate(2, add=3, multiply=5))