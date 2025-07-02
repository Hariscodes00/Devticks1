#1 Write a program that checks if a number is positive, negative, or zero.
num1 = 0
if num1 > 0 :
    print("the number is positive")
elif num1 < 0 :
    print("The number is negative")
else :
    print("the number is zero")

#2 Create a program to check if a person is eligible to vote. (age ≥ 18)
age = int(input("please enter your age: "))
if age >= 18 :
    print("you can vote")
else:
    print("you are ineligible to vote")

#3 Ask the user for their name, and print "Welcome" only if the name is not empty.
User = input("please enter your name: ")
if User == "" :
    print("Welcome")
else :
    print("name not found")

#4 Write a program that takes a number from the user and prints: "Even" if it’s even "Odd" if it’s odd
check = int(input("enter any number: "))
if check%2 == 0 :
    print("it's even")
else :
    print("it's odd")

#5 Create a program that takes a temperature value, and prints: "Cold" if below 10 "Warm" if between 10 and 25 "Hot" if above 25
temp = int(input("enter your city's temperature: "))
if temp > 10 :
    print("Cold")
elif 10<=temp <=25 :
    print("Warm")
else :
    print("hot")