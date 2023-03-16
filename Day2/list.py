#list -- Ordered
list1=[10,20.2,2+3j,"Hi",True]
print(list1)
print(type(list1))
list2=list([10,20.2,2+3j,"Hi",True])
print(list2)
list1.append(786) #takes only 1 argument
print(list1)
list1.extend([69,'six','nine']) #takes more than 1 argument
print(list1)
list1.insert(4,'lol') #insert at index 4
print(list1)
list1.pop(4) # del/pop from index 4
print(list1)
del list1[4]# del/pop from index 4
print(list1)


