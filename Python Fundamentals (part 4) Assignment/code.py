from abc import ABC, abstractmethod


# Q1
class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(f"Account balance is:{self.balance}")


b1 = BankAccount("1234Ab", "Abdullah", 60_000)
b1.deposit_money(10_000)
b1.withdraw_money(5000)
b1.check_balance()


# Q2
class Book:
    def __init__(self, title, author, list_of_reviews):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews

    def add_review(self, review):
        self.list_of_reviews.append(review)

    def count_reviews(self):
        print(len(self.list_of_reviews))

    def display_all_reviews(self):
        print(self.list_of_reviews)


b1 = Book("Sapiens", "Yuval Noah Herrari", ["excellent"])
b1.add_review("Life Changing")
b1.count_reviews()
b1.display_all_reviews()


# Q3
class Student:

    def __init__(self, name, rollno, marks):
        self.__name = (self.set_name(name),)
        self.__rollno = (self.set_rollno(rollno),)
        self.__marks = (self.set_marks(marks),)

    def set_name(self, name):
        if name == "":
            return print("Name cannot be empty")
        self.name = name

    def set_rollno(self, rollno):
        if rollno < 0 or rollno > 100:
            return print("rollno should be between 1 & 100")
        self.rollno = rollno

    def set_marks(self, marks):
        if marks < 0:
            return print("marks should be positive")
        self.marks = marks

    def get_name(self):
        print(f"{self.name}")

    def get_rollno(self):
        print(f"{self.rollno}")

    def get_marks(self):
        print(f"{self.marks}")


st1 = Student("Abdullah", 21, 91)
st2 = Student("", 21, 91)
st3 = Student("Abdullah", 101, 91)
st4 = Student("Abdullah", 21, -1)
st1.get_marks()
st1.get_name()
st1.get_rollno()


# Q4
class Shape:
    PI = 3.14

    def get_area(self):
        print("Area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(f"{self.PI*self.radius**2}")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        print(f"{self.length*self.width}")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        print(f"{1/2*self.base*self.height}")


shape1 = Shape()
shape2 = Circle(25)
shape3 = Rectangle(10, 20)
shape4 = Triangle(5, 10)
shape1.get_area()
shape2.get_area()
shape3.get_area()
shape4.get_area()


# Q5
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


vehicle = Vehicle("Honda", "City")
car = Car("Toyota", "Corolla", 5)
bike = Bike("Honda", "125", "125")


# Q6
class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass


class Intern(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f"{self.salary}")


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f"{self.salary}")


class ContractEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f"{self.salary}")


intern = Intern(25000)
full_time_employee = FullTimeEmployee(50000)
contract_employee = ContractEmployee(35000)
intern.calculate_salary()
full_time_employee.calculate_salary()
contract_employee.calculate_salary()


# Q7
class Person:
    def __init__(self, name, age=18, address="Panjab"):
        self.name = name
        self.age = age
        self.address = address


p1 = Person("Abdullah")
p2 = Person("Abdullah", 21)
p3 = Person("Abdullah", 21, "Sambrial")


# Q8
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1


p1 = Player("Abdullah", 21)
p2 = Player("Bhatti", 69)
print(Player.player_count)


# Q9
class Herbivore:
    def __init__(self, plant):
        self.plant = plant

    def herb_eat(self):
        print(f"I eat plants")


class Carnivore:
    def __init__(self, meat):
        self.meat = meat

    def carn_eat(self):
        print("I eat meat")


class Omnivore:
    def __init__(self, food):
        self.food = food

    def omni_eat(self):
        print("I eat both plants and animals")


class Beer(Herbivore, Carnivore, Omnivore):
    def __init__(self, plant, meat, food, activity):
        super().__init__(plant)
        Carnivore.__init__(self, meat)
        Omnivore.__init__(self, food)
        self.activity = activity

    def favorite_activity(self):
        print(f"My favorite activity is {self.activity}")


b1 = Beer("hops", "beef", "nuts", "water playing")
print(b1.plant)
print(b1.meat)
print(b1.food)
print(b1.activity)
b1.herb_eat()
b1.carn_eat()
b1.omni_eat()
b1.favorite_activity()


# Q10
class ChatRoom:
    chat_history = []
    join_leave = []


class User(ChatRoom):
    def __init__(self, name):
        self.name = name

    def join_room(self):
        print(f"{self.name} joined")
        self.join_leave.append(f"{self.name} joined")

    def leave_room(self):
        print(f"{self.name} left")
        self.join_leave.append(f"{self.name} left")


class Messages(ChatRoom):
    def __init__(self, message):
        self.message = message
        self.chat_history.append(message)


user1 = User("Abdullah")
user1.join_room()
msg = Messages("Hey")
user1.leave_room()
print(ChatRoom.chat_history)
print(ChatRoom.join_leave)
