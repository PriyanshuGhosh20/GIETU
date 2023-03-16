list_a=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
for i in list_b:
    print(f'({i},{list_a.index(i)})')

#Using List Comprehension
print("By List Comprehension: ")
print([(i,list_a.index(i)) for i in list_b])
print()

#Using dictionary
print("Dictionary:- ")
dic={}
for i in list_b:
    dic[i]=list_a.index(i)
print(dic)

print("By Dictionary Comprehension: ")
print({i:list_a.index(i) for i in list_b})

