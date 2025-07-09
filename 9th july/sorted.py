#sorting list
lis = [1,2,3,7,8,9,5,4]
lis.sort()  #using sort method
print('using sort method:\t',lis)
lis_sorted = sorted(lis , reverse=True)     #Appling sorted function
print('using sorted function:\t',lis_sorted )

#sorting tuple
tup = (1,2,3,7,8,9,5,4)
#print(tup.sort())    error
tup_sorted = sorted(tup)    #Appling sorted function
print('sorted tuple:\t',tup_sorted)    #returns a sorted list
print('original tuple:\t' , tup)
#sorting dic
dic= {"name" : "haris", "age":"21" , 'edu':'bachelors'}
#print(dic.sort()) error
dic_sorted = sorted(dic)      #Appling sorted function
print('sorted dic:\t' , dic_sorted) #return list of keys
print('original dic :\t' , dic)
