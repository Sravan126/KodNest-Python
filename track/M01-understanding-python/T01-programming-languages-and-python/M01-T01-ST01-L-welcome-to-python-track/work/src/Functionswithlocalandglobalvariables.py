# 1. Global variable inside a function

c = 30

def add():
    global a
    a = 10
    b = 20  # Local variable

    print(a + b)
    print(c)  # Global variable

add()


# 2. Local variable vs Global variable

x = 100  # Global variable

def display():
    x = 50  # Local variable
    print("Local x:", x)

display()
print("Global x:", x)


# 3. Accessing a global variable inside a function

x = 10  # Global variable

def display():
    print(x)
    # x = 20  # Local variable
    print(x)

display()

x = 30
print(x)