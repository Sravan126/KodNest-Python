
# ==========================================
# PYTHON OPERATORS - COMPLETE NOTES
# ==========================================


# 1. ARITHMETIC OPERATORS
# Used to perform mathematical calculations.

# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# %  Modulus (Returns remainder)
# ** Exponentiation (Power)
# // Floor Division (Rounds down)

print("----- ARITHMETIC OPERATORS -----")

print(3 + 3)      # 6
print(3 - 3)      # 0
print(3 * 3)      # 9
print(1 / 3)      # 0.3333333333333333
print(100 % 30)   # 10
print(3 ** 3)     # 27
print(10 // 3)    # 3


# 2. COMPARISON OPERATORS
# Used to compare two values.
# Output will always be True or False.

# == Equal to
# != Not equal to
# >  Greater than
# <  Less than
# >= Greater than or equal to
# <= Less than or equal to

print("----- COMPARISON OPERATORS -----")

print(11 == 10)   # False
print(11 != 10)   # True
print(11 > 10)    # True
print(11 < 10)    # False
print(11 >= 10)   # True
print(11 <= 10)   # False


# 3. ASSIGNMENT OPERATORS
# Used to assign and update variable values.

# =   Assignment
# +=  Addition assignment
# -=  Subtraction assignment
# *=  Multiplication assignment
# /=  Division assignment
# %=  Modulus assignment
# **= Exponentiation assignment
# //= Floor division assignment

print("----- ASSIGNMENT OPERATORS -----")

a = 10
print(a)       # 10

a += 10
print(a)       # 20

a -= 10
print(a)       # 10

a *= 10
print(a)       # 100

a /= 10
print(a)       # 10.0

a %= 10
print(a)       # 0.0

a **= 2
print(a)       # 0.0

a = 2
a //= 2
print(a)       # 1


# 4. LOGICAL OPERATORS
# Used to combine multiple conditions.

# and - Both conditions must be True.
# or  - At least one condition must be True.
# not - Reverses the Boolean value.

print("----- LOGICAL OPERATORS -----")

a = False
b = False

print(a and b)    # False
print(a or b)     # False
print(not a)      # True
print(not b)      # True

a = (5 > 3) and (4 < 6)
print(a)          # True

a = (5 < 3) or (4 < 6)
print(a)          # True

a = not (5 > 3)
print(a)          # False


# 5. IDENTITY OPERATORS
# Used to check whether two variables
# refer to the same object in memory.

# is     - Same object
# is not - Different objects

print("----- IDENTITY OPERATORS -----")

a = 10
b = 10

print(a is b)       # True
print(a is not b)   # False

# Difference between is and ==

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)       # True (Same values)
print(a is b)       # False (Different objects)


# 6. MEMBERSHIP OPERATORS
# Used to check whether an element
# exists inside a collection.

# in     - Element exists
# not in - Element does not exist

print("----- MEMBERSHIP OPERATORS -----")

a = [1, 2, 3, 4, 5]

print(1 in a)       # True
print(6 in a)       # False
print(1 not in a)   # False
print(6 not in a)   # True


# 7. BITWISE OPERATORS
# Perform operations on binary numbers (0 and 1).

# &  Bitwise AND
# |  Bitwise OR
# ^  Bitwise XOR
# ~  Bitwise NOT
# << Left Shift
# >> Right Shift

print("----- BITWISE OPERATORS -----")

a = 2
b = 3

print(a & b)       # 2 (AND)
print(a | b)       # 3 (OR)
print(a ^ b)       # 1 (XOR)

a = 5

print(~a)          # -6 (NOT)
print(a << 3)      # 40 (Left Shift)
print(a >> 3)      # 0 (Right Shift)


# ==========================================
# IMPORTANT PYTHON CONCEPTS
# ==========================================

# 1. Assignment vs Comparison

a = 10             # Assigns value
print(a == 10)     # Compares value


# 2. Boolean values

print(True)        # True
print(False)       # False

# True behaves like 1 in arithmetic.
# False behaves like 0 in arithmetic.

print(True * 20)   # 20
print(False * 20)  # 0


# 3. Boolean conversion

print(bool("True"))    # True
print(bool("False"))   # True (Non-empty string)
print(bool(""))        # False

# Correct way to convert user input
user_agreement = input().strip().lower() == "true"
print(user_agreement)


# 4. Real-life example using operators

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


# 5. Event fee calculation

contribution_amount = 50.0
needs_transportation = True

total_fee = contribution_amount + 20 * needs_transportation

print("Total Fee:", total_fee)  # 70.0


# ==========================================
# QUICK REVISION
# ==========================================

# Arithmetic:    + - * / % ** //
# Comparison:    == != > < >= <=
# Assignment:    = += -= *= /= %= **= //=
# Logical:       and or not
# Identity:      is, is not
# Membership:    in, not in
# Bitwise:       & | ^ ~ << >>

# ==========================================
# END OF PYTHON OPERATORS
# ==========================================
