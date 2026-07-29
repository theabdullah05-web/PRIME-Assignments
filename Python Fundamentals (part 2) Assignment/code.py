# Q1
salary = int(input("Write your salary: "))
if salary < 30000:
    print("Tax: 5%")
elif salary >= 30000 and salary <= 70000:
    print("Tax: 15%")
else:
    print("Tax: 25%")

# Q2
a = int(input("Write 1st number: "))
b = int(input("Write your 2nd number: "))


def even(n1, n2):
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            print(i)


even(a, b)

# Q3
n = int(input("Write the number: "))


def digits(N):
    while N / 10 > 0:
        right_num = N % 10
        print(int(right_num))
        N = N // 10


digits(n)

# Q4
n = int(input("Write the number: "))
count = 0
while n / 10 > 0:
    count += 1
    n = n // 10
print(count)

# Q5
n = int(input("Write the number: "))
sum = 0
while n / 10 > 0:
    sum_num = n % 10
    sum += sum_num
    n = n // 10
print(sum)


# Q6
def print_to_hundred():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)


print_to_hundred()

# Q7
while True:
    input1 = input("write a number: ")
    if input1 == "Quit":
        break
    n = float(input1)
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("0 is neither positive nor negative")


# Q8
def calculator(a, b, operation):
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        print(a / b)


calculator(16, 8, "/")


# Q9
def is_Prime(n):
    for i in (2, n - 1):
        if n % i == 0:
            return False
        else:
            return True


print(is_Prime(4))

# Q10
answer = 21
guess = int(input("Write your guess: "))
while guess != answer:
    guess = int(input("Wrong guess!!! Retry: "))
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too Low")
    elif guess == answer:
        print("Correct")
