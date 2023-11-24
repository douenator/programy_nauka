def decorator(func):
    def wrapper():
        print("----------")
        func()
        print("----------")
    return wrapper

def hello():
    print("Hello World")

hello = decorator(hello)
hello()

print()

@decorator
def witaj():
    print("witaj świecie")

witaj()