#simple calculator takes 2 inputs and apply 4 operations ( add , sub , div , mul )

def add (a,b) :   #add function
    return a+b
def sub (a,b) :   #subtract function
    return a-b
def mul (a,b) :   #multiply function
    return a*b
def div (a,b) :   #divide function
    return a/b

#making variables to take input
num1 = float(input("please enter first number : "))
num2 = float(input("please enter second number : "))

#displaying operations
print("please select operation")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

#taking operation choice
op = int(input("Please select operation '1/2/3/4' :  "))

#applying function on command
if op == 1:
    print(f"The result is :{add(num1,num2)}")
elif op == 2:
    print(f"The result is: {sub(num1,num2)} ")
elif op == 3:
    print(f"The result is: {mul(num1, num2)} ")
elif op == 4:
    print(f"The result is: {div(num1, num2)} ")
else:
    print("invalid entry")