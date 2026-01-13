#Write a Python program that
#1Repeatedly asks the user to enter a word (using a while loop).
#2If the word length is less than 3, skip it (using continue).
#3If the word is "stop", end the loop immediately (using break).
#4Otherwise, print the word in uppercase.
#5After the loop ends, print:
#6Program ended.

while True :
    word = input("please enter a word :")
    if word == "stop" :
        break
    if len(word) < 3 :
        continue
    else :
        print(word.upper())
print("program ended")

