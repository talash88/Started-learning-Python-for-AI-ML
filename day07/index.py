
# This code demonstrates two tuple methods: count() and index(). Here's what each line does:


a = (1,45,324,2345,False, 45, "Harsh","Afaq")
print(a)
no = a.count(45)
print(no) 

i = a.index(45)
print(i)


# Multiple-Element Tuple
t = tuple("Python")
print(t)


# Multiple-Element Tuple


t3 = (10, 20, 30, 40)
print(t3)


# Homogeneous Tuple (Same Data Type)
numbers = (1, 2, 3, 4, 5)
names = ("Harsh", "Afaq", "Rahul")


# Nested Tuple


nested = ((1, 2), (3, 4), (5, 6))
print(nested)


# Tuple Without Parentheses (Packing)
t = 10, 20, 30
print(t)


# Repeated Tuple

t = ("SHRUTI",) * 5
print(t)



# Concatenated Tuple

a = (1, 2, 3)
b = (4, 5, 6)

c = a + b
print(c)


# Tuple with Duplicate Values
t = (True, False, True)
print(t)


# Tuple with Mixed Objects
t = (10, [1, 2], {"name": "Harsh"}, (5, 6))
print(t)

