start=int(input())
end=int(input())

#1List Comprehension
arr=[]
for i in range(start,end+1):
    arr.append(i)
print(arr)
#arr = [i for i in range(start,end+1)]
#print(arr) #[1,2,3]
sub=[]
for i in range(len(arr)): #i=1
    for j in range(i,len(arr)): #j=1,2
        sub.append(arr[i:j+1]) #[0:1]=[1],[0:2]=[1,2]
print(sub)
