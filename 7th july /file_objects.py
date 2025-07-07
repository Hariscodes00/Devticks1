f = open ('test.txt' , 'r')
f_context = f.read(15)
print(f_context)

f_context = f.read(15)
print(f_context)

#file context managament

# with open ('test.txt' , 'r+') as f:
    #f_context = f.read(15)
    #print(f_context)
    #f_test = f.readlines()
    #print(f_test)
#    for lines in f:
#       print(lines , end = '')

# with open ('test.txt' , 'r+') as f:
#   size_to_read = 10
#   f_context = f.read(size_to_read)
#    while len(f_context) > 0:
#     print(f_context , end = '*')
#       f_context = f.read(size_to_read)


# with open ('test.txt' , 'r+') as f:
#    size_to_read = 10
#    f_context = f.read(size_to_read)
#    print(f.tell())

#writing and copying the files
with open ('test.txt','r') as rf:
    with open ('test2.txt', 'w') as wf:
        for lines in rf :
            wf.write(lines)

# copying image
with open('graphics card.jpg','rb') as jf:
    with open('rtx 3090.jpg' , 'wb') as jw:
        for line in jf:
            jw.write(line)