# file name = main.py
# Student Name = Sabit Hasan

# Variables and data types
name = "Sabid"
age = 20
student = True

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Is student:",  student, "Type:", type(student))



# Arithmetic operations
print("Age + 5 =", age + 5)
print("Age - 2 =", age - 2)
print("Age * 2 =", age * 2)
print("Age / 2 =", age / 2)


# Comparison operators
print("Is age > 18?", age > 18)
print("Is age == 20?", age == 20)
print("Is age != 15?", age != 15)
print("Is age > 30?", age > 30)


# Logical operators
has_id = True
is_adult = age >= 18
print("Has ID and Is Adult:", has_id and is_adult)
print("Has ID or Is Minor:", has_id or age < 18)
print("Not a student:", not  student)



# Assignment operator
a = 10
print("Initial Number:", a)

a += 5
print("After += 5:", a)

a -= 2
print("After -= 2:", a)

a *= 3
print("After *= 3:", a)

a /= 2
print("After /= 2:", a)



# Identity operator
x = 10
y = 10
z = 15

print("x is y? Ans is=", x is y)
print("x is y? Ans is=", x is z)
print("x is not z? Ans is=", x is not z)
print("x is not z? Ans is=", y is not z)



# Membership Operator
f = ["apple", "banana", "mango"]

print("'apple' is a fruits? Ans is=", "apple" in f)
print("'grape' is not fruits? Ans is=", "grape" not in f)
