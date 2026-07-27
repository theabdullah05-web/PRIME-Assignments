# Q1
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello,", name, "you are", age, "years old!")

# Q2
n1 = float(input("Write 1st number: "))
n2 = float(input("Write 2nd number: "))
print("addition:", n1 + n2)
print("difference:", n1 - n2)
print("product:", n1 * n2)
print("quotient:", n1 / n2)

# Q3
n1 = float(input("Write 1st integer:"))
n2 = float(input("Write 2nd integer:"))
n3 = float(input("Write the float:"))
avg = (n1 + n2 + n3) / 3
print(avg)

# Q4
string1 = input("Enter string:")
integer1 = int(string1)
float1 = float(string1)
print(string1, type(string1))
print(integer1, type(integer1))
print(float1, type(float1))

# Q5
x = 10 + 3 * 2**2
"""
x will be equal to 22 because of arithmetic operators and operators precedence
"""

# Q6
a = float(input("Write 1st number: "))
b = float(input("Write 2nd number: "))
print("originaly a is:", a)
print("originaly b is:", b)
c = a
d = b
a = d
b = c
print("now a is:", a)
print("now b is:", b)
