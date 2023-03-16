list1=[3,4,1,8,5,9,0,6]
n=9
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if i+j==n:
            list1=[i,j]
            print(list1)
            count=count+1
print(count)
