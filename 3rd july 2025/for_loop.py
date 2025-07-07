# for-loop in list
#1 Given a list of integers [5, 10, 15, 20], print each element multiplied by 2.
a = [5, 10, 15, 20]
for x in a :
    print(x*2)

#2 From the list ["apple", "banana", "cherry"], print each fruit in uppercase letters.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())

#3 You have a list of numbers [1, 2, 3, 4, 5]. Use a for loop to print only the even numbers.
nums = [1, 2, 3, 4, 5]
for num in nums :
    if num%2 == 0:
     print(num)

#4 Given ["car", "bike", "train"], print the position and the vehicle using enumerate.
vehicles = ["car", "bike", "train"]
for index , vehicle in enumerate(vehicles):
    print(f"Index{index} : {vehicle}")
#5 Make a list of 5 random names and print a greeting to each, for example:
names = [ "haris","ahmed","ali","hamza","adnan"]
for name in names:
    print(f"Hello {name}")
#------------------------------------------------------------------------------------------
# tuples in for-loop
#1 Given a tuple of coordinates (10, 20, 30, 40), print each coordinate value
coordinates = (10, 20, 30, 40)
for index , value in enumerate(coordinates):
    print(f"index {index}, value {value}")

#2 You have a tuple of colors ("red", "green", "blue"). Print the color name and its length (number of letters).
colors = ("red", "green", "blue")
for color in colors:
    print (f"{color} : {len(color)}")

#3 Tuple of numbers (2, 4, 6, 8) — print each number squared.
numbers = (2, 4, 6, 8)
for number in numbers:
    print(number*number)

#4  From ("Ali", "Fatima", "Sara"), print a statement:"[name] is present"
names = ("Ali", "Fatima", "Sara")
for name in names :
    print(f"{name} is present")

#5 A tuple of temperatures (22, 24, 26). Convert each to Fahrenheit and print the result.
temperatures = (22, 24, 26)
for temp in temperatures:
    print((temp*1.8)+32)

#-------------------------------------------------------------------------------------------
#for loop in set
#1 Given a set {1, 2, 3, 4, 5}, print each element multiplied by 10.
set1 = {1, 2, 3, 4, 5}
for elm in set1:
    print(elm*10)

#2 From the set {"dog", "cat", "rabbit"}, print each animal with the phrase: "I love [animal]"
animals = {"dog", "cat", "rabbit"}
for animal in animals :
    print(f"I Love {animal}")

#3 There is a set of odd numbers {3, 5, 7, 9} — print only numbers greater than 5.
odd = {3, 5, 7, 9}
for od in odd :
    if od<=5:
        continue
    print(od)

#4 Set of subjects {"Math", "Science", "English"} — print each subject in lowercase.
subjects = {"Math", "Science", "English"}
for subject in subjects :
    print(subject.lower())

#5 A set of cities {"Lahore", "Karachi", "Islamabad"} — print each city with its name length.
cities = {"Lahore", "Karachi", "Islamabad"}
for city in cities :
    print(f"{city} : {len(city)}")

#-----------------------------------------------------------------------------------
#for-loop in dictionaries

#1 Given {"Ali":90, "Fatima":80, "Zara":95}, print each name and their marks.
marks = {"Ali":90, "Fatima":80, "Zara":95}
for  mark in marks:
    print(f"{mark} : {marks[mark]}")

#2 From {"apple":50, "banana":30}, print only the keys (fruit names).
fruit1 = {"apple":50, "banana":30}
for f in fruit1:
    print(f)

#3 Using {"pen":10, "pencil":5, "eraser":7}, print only the values
stationary = {"pen":10, "pencil":5, "eraser":7}
for key , value in stationary.items():
    print({value})

#4 Dictionary of capitals {"Pakistan":"Islamabad", "India":"Delhi"}, print each country with its capital nicely formatted.
capitals = {"Pakistan":"Islamabad", "India":"Delhi"}
for key1 , value1 in capitals.items():
    print(f"{key1} : {value1}")

#5 A dictionary {"a":1, "b":2, "c":3} — print only key-value pairs where the value is greater than 1.
pairs = {"a":1, "b":2, "c":3}
for keys , values in pairs.items() :
    if values > 1:
     print(f"{keys} : {values}")

#---------------------------------------------------------------------

#Write a Python program that:
#1. Accepts a list of integers from the user.
#2. Loops through the list and prints out each number.
#3. If a number is greater than 10, skips it using the continue statement.
#4. Stops the loop if the number is 20 using the break statement.
#5. After the loop ends, prints a message that the loop ended naturally

User = input("Enter a list of integers seperated by space : ")
numbers = list(map(int, User.split()))
for num in numbers :
    if num > 10 :
        continue
    if num >=20 :
        break
    print(num)
print("loop ended")