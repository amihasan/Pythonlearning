"""
Variable: it is a container to a value.

"""

# How will i get a memory address?

rol_number = 12584.0
print(id(rol_number))

# to know what type of data is stored

print(type(rol_number))

"""
VARIABLES RULES (LEXICAL WAY)

variable ::= (letter | "_")(letter | digit | "_")
letter ::= lowercase | uppercase
lowercase ::= "a" ... "z"
uppercase ::= "A" ... "Z"
digit ::= 0 ... 9
"""

#  Reserved keywords cannot be used as variable names.
# 32 reserved items

import keyword

print(keyword.kwlist)


# How do we define the variables ?
# variable_name = value

name, age, dept_id = "Ashish", 30, 123456
print(name)
print(age)
print(dept_id)

Department_ID = d_ID = 23456
print(Department_ID)
print(d_ID)

"""
HOW DO WE SWAP VALUES ? 
"""

a, b = 10, 30
print("Before A= ", a)
print("Before B= ", b)
a,b = b, a

print("After A= ", a)
print("After B= ", b)

"""
DATA TYPES PYTHON SUPPORTS

1. INTEGERS
2. FLOAT
3. STRINGS
4. COMPLEX NUMBERS
5. LIST
6. TUPLES
7. DICTIONARY
8. SET

"""


# age = 30
# print(type(age))
#
# salary = 10000.50
# print(type(salary))
#
# print(2e5)

