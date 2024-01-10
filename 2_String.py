"""
String

"""

# How do we access a string?

institution = "Way2Automation"
print(institution)
print(type(institution))

print(institution[3])
print(institution[4])
print(institution[6])
# print(institution[100]) # IndexError: string index out of range
print(institution[-1])

"""
SLICING OPERATION
"""

# What is slicing?
# Slice is an operation which help to get specific string.

"""
How to get a substring out of a string. 

    variableName[begin:end:step]
    
    begin ::= The index value where the slicing to be started
    end ::= The index value until where the slicing is to be done. 
    step ::= This determines the increment / decrement for each index of slice

"""

example = "abcdefghij"

print(example)
print(example[0:4])  # abcd
print(example[2:4])  # cd
print(example[2:10:2])  # cegi
print(example[:])  # abcdefghij
print(example[7:4:-1])  # hgf
print(example[9:1:-2])  # jhfd
print(example[:100000])  # abcdefghij
print(example[2:7:-1])  # nothing will be printed
print(example[::-1])  # jihgfedcba

"""
String formatters 

Hey, My name is - "Ahmed"

1. Using format()
2. % Operator
    string --> %s
    int --> %d
    float --> %f
3. f-strings

"""

name = "Ahmed"
age = 45
address = "Avon"

print("Hey, my name is {0}. I am {1} years old and i live in {2}.".format(name, age, address))
print("Hey, my name is %s. I am %d years old and i live in %s" % (name, age, address))
print(f"Hey, my name is {name}. I am {age} years old and i live in {address}.")


"""
String Operations and Functions
"""
e2 = "Example for string and function"
e3 = "33"

# How to get the length of any string?

print(len(e2))

# How to convert strings to different types of cases ?

print(e2.upper())
print(e2.lower())
print(e2.title())

# How to identify if the string is a digit or not ?

print(e3.isdigit())
print(e2.isalpha())

# What is the output for the following :
print('10' + '20')  # 1020
print('ba' + 'na' * 2)  # banana

# Verify nana is in banana ?
# in --> MEMBERSHIP OPERATOR

print('nana' in 'banana')
print('nanana' not in 'banana')

