s="3,2,6,5,1,4,8,9"
arr=list(map(int,s.split(',')))
print(arr)
num1=sum(arr[:arr.index(5)])+sum(arr[arr.index(8)+1:])
print(num1)
l=arr[arr.index(5):arr.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(num2)
print(f'{num1} + {int(num2)} = {int(num2)+num1}')
