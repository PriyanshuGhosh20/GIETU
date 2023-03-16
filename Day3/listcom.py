"""
res=[]
#Even Elements
#Using for loop
for i in range(11):
    if i%2==0:
        res.append(i)
print(res)
#List Comprehension
res=[i for i in range(11,21) if i%2==0]
print(res)

#Odd Elements
res1=[]
for i in range(1,11,2):
    res1.append(i)
print(res1)
#List Comprehension
res1=[i for i in range(11,21) if i%2!=0]
print(res1)

#if even square else original
print([i if i%2!=0 else i**2 for i in range(11) ])
print()
"""

#Square the Odd, Cube the Even Elements
#1D
print("Square the Odd & Cube the Even Elements:-\n")
print("In One Dimension (1D): ")
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res=[]
for i in mat:
    for j in i:
        if j%2==0:
            res.append(j**3)
        else:
            res.append(j**2)
print(res)

#ListComprehension
print("By List Comprehension (1D): ")
print([j**3 if j%2==0 else j**2 for i in mat for j in i])
print()
#2D
print("In Two Dimension (2D): ")
res=[]
for i in mat:
    res1=[]
    for j in i:
        if j%2==0:
            res1.append(j**3)
        else:
            res1.append(j**2)
    res.append(res1)
print(res)

#ListComprehension
print("By List Comprehension (2D): ")
print([[j**3 if j%2==0 else j**2 for j in i] for i in mat])

