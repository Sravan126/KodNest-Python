# 1. Function overloading examples

def add(a, b):
    print(a + b)

def add(a, b, c):
    print(a + b + c)

def add(a, b, c, d):
    print(a + b + c + d)

# Python does not support traditional function overloading.
# The latest function definition replaces the previous ones.

add(10, 20, 30, 40)  # 100


# 2. Default values

def add(a, b=0, c=0):
    print(a + b + c)

add(10, 20)      # 30
add(10, 20, 30)  # 60
add(10)          # 10


# 3. *args - Variable number of arguments

def add(*a):
    print(sum(a))

add(10, 20)       # 30
add(10, 20, 30)   # 60
add(10)           # 10
add()             # 0


# 4. **kwargs - Variable number of keyword arguments

def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name')}", end=" ")
    print(f"Age is {kwargs.get('age')}", end=" ")
    print(f"Course is {kwargs.get('course')}")

stu_info(name="Shubham", age=21, course="python")