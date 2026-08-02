# Q1
name = input("Write your name: ")
name1 = input("Write your name: ")
name2 = input("Write your name: ")
name3 = input("Write your name: ")
name4 = input("Write your name: ")
with open("names.txt", "w") as f:
    f.write(name + "\n" + name1 + "\n" + name2 + "\n" + name3 + "\n" + name4)

with open("names.txt", "r") as f:
    data = f.read()
    print(data)

# Q2
with open("logs.txt", "a") as f:
    f.write("\nProgram run successfully")
with open("logs.txt", "r") as f:
    data = f.read()
    print(data)

# Q3
li = [5, 10, 15, 20, 25]
new_li = [i for i in li if i > 15]
print(new_li)

# Q4
import json

cities = {"Koyoto": 1460000, "Calgary": 1340000, "Porto": 231000}
with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)
with open("cities.json", "r") as f:
    data = json.load(f)
    print(data)
new_city = input("Enter a new city: ")
population = int(input("Its population: "))
with open("cities.json", "w") as f:
    cities.update({new_city: population})
    json.dump(cities, f, indent=4)

# Q5
try:
    with open("data.txt", "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File Not Found")
