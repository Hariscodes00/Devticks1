# f = open(sort.py)
# try :
#     f = open(sort.py)
# except SyntaxError :
#     print("syntac error")
# except NameError :
#     print("Name error")
# except Exception :
#     print('file was not found')

#else for result
try :
    f = open('sorted.py') #try to open file
except SyntaxError : #lookout for syntax error
    print("syntac error")
except NameError : #lookout for name error
    print("Name error")
except Exception : #lookout for all errors and exception not specific
    print('file was not found')
else:
    print(f.read())
    f.close()   #else to open file or make decisions after it pass the test
finally:
    print('testing completed.....') #finally will execute no matter what