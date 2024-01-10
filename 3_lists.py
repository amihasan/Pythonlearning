"""

List
Python List

    --> Collection of Heterogeneous items.
    --> String, int, float etc.
    --> Order is maintained(order of adding seq).
    --> Duplicate items can be added.
    --> List is used []
    --> Mutable in nature:
        1. Create a list
        2. Read/ Access a list
        3. Update a list
        4. Delete a list
    --> CRUD operations

"""

"""
Creating a List
"""

# How to create a empty list?

empty = []
print(type(empty))
print(empty)

# How to create regular list?

regular = ["Ahmed", 45, "Avon", True, "ETL Lead"]

print(regular)
print(type(regular))

# Can a list contain another list?

sublist = [["Ahmed", "", "Hasan"], ["SQL", "Data Warehouse", "Python", "Manual", "Automation"], 45, "40 Orchard ST"]
print(sublist)

# Can we convert a String into a list

place = "Bangladesh"
print(place)
print(list(place))

# Create a list with first 10 integer

"""
    range(begin, end, step)
        begin ::    From where to start ?
        end ::      Where to stop ? 
        step ::     increment / decrement ?     
    END is not always included
"""
first10integers = list(range(0, 10, 1))
print(first10integers)

"""
READ / ACCESS A LIST
--> Index values always starts from 0.
"""

example = ["Ashish", 1, 2, 3, 4.5, ["Abhishek", True, 4 + 3j], 5, ("Shashank", 34, 2.3), 6, {"name": "Ahmed"}]
print(example)

# How is the order maintained in a list?

print(example[0])
print(example[5])
print(example[5][0])

# How to we read inside a multidimensional list ?

multi = [
    [1, 2, 3, ["A", "B", ["C", ["D"]]]],
    [4, 5, 6],
    [7, 8, 9]
]
print(multi[0])
print(multi[2])
print(multi[0][1])
print(multi[1][2])
print(multi[0][3][2][0])

# Can we access multiple items from a list?
# SLICING Operation is supported in a list.
print(example[0:3])


"""
UPDATING A LIST 
"""

# Can we update a complete list ?

shopping_item = ["T-Shirt", "Glasses", "Shoes"]
print(shopping_item)
shopping_item = [10, 20, 32, "Bag"]
print(shopping_item)

# Can we update a single item in a list ?

shopping_item = [10, 20, 32, "Bag"]
shopping_item[2] = 'Fruits'
print(shopping_item)


# Can we update multiple items in a list ?

shopping_item = [10, 20, "Fruits", 40, "Bag"]
shopping_item[0:3] = [1, 2, "Milk"]
print(shopping_item)

# What will happen if I give the last + 1 index value to update ?

