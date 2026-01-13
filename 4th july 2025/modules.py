#importing square function from math.py
from funcions import square

#using to print value
result = square(12)
print(f"The square of 12 is {result}")

#importing all functions from math.py
from funcions import *

#importing random
import random

# 1. Randomly select a number between 1 and 100
num = random.randint(1 ,100)

# 2. Check if even or odd
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")