def call_once(func):
    called = False
    def wrapper():
        nonlocal called
        if not called:
            called = True
            func()
        else:
            print("Function can be called only once")
    return wrapper
@call_once
def greet():
    print("Hello, Welcome!")
greet()
greet()
