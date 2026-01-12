#6 l3
def my_decorator(func): # Outer function
    def wrapper(): # Inner function (closure)
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper # Return inner function
@my_decorator
def say_hello():
    print("Hello, World!")
say_hello()
