# Q1
string = "abdullah"
li = []
reverse_li = []
for char in string:
    li.append(char)
for char in string:
    reverse_li.append(char)
reverse_li.reverse()


if li != reverse_li:
    print("Not A Palindrome")
else:
    print("Palindrome")

# Q2
li = [10, 15, 20, 25]
sum = 0
count = 0
for i in li:
    sum += i
    count += 1
avg = sum / count
print(avg)

# Q3

list1 = [1, 2, 7]
list2 = [2, 4, 5]
result = []
for i in list1:
    result.append(i)
for i in list2:
    result.append(i)
result.sort()
print(result)

# Q4
even_list = []
odd_list = []
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in list1:
    if i % 2 == 0:
        even_list.append(i)
    elif i % 2 != 0:
        odd_list.append(i)
even_tuple = tuple(even_list)
odd_tuple = tuple(odd_list)
print(even_tuple, type(even_tuple))
print(odd_tuple, type(odd_tuple))

# Q5
dict1 = {"abdullah": 21, "shradha": 99, "aman": 99}
key = input("Enter your key: ")
while True:
    key = input("Enter your key: ")
    if key == "quit":
        break
    elif key == "A":
        name = input("Enter student name: ")
        marks = float(input("Write marks: "))
        dict1.update({name: marks})
    elif key == "B":
        name = input("Enter student name: ")
        marks = float(input("Write marks: "))
        dict1.update({name: marks})
    elif key == "C":
        name = input("Enter student name: ")
        info1 = dict1.get(name)
        if dict1.get(name) == None:
            print("Student doesn't exist")
        elif dict1.get(name) != None:
            print(f"{name}'s marks:{info1}")
    elif key == "D":
        print(dict1.items())
    else:
        print("Enter a valid command")

# Q6
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict1 = {}
for i in words:
    length = len(i)
    dict1.update({i: length})
print(dict1)

# Q7
string = "Fear is for lesser men"
count = 0
for i in string:
    if i == " ":
        count += 1
print(f"There are {count} spaces in the given string")

# Q8
li1 = [1, 2, 3, 4, 5]
li2 = [1, 2, 8, 3, 0]
check = []
for i in li1:
    check.append(i)
for i in li2:
    check.append(i)
check_set = set(check)
if len(check) == len(check_set):
    print("These lists donot share any common element")
else:
    print(f"These lists share {len(check)-len(check_set)} common elements")


# Q9
li5 = [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 8]
s = set()
twice = set()
for i in li5:
    if i in s:
        twice.add(i)
    else:
        s.add(i)
print(f"these elements come more than twice {twice}")

# Q10
string = input("Enter your string: ")
s = set()
for i in string:
    s.add(i)
print(f"These are all the unique characters: {s} and there count is {len(s)}")
