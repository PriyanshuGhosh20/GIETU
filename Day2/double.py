num=int(input())
dnum=2*num
flag=0
str1=str(num)
str2=str(dnum)
for i in str1:
    if i in str2:
        continue
    else:
        flag=flag+1
if flag>0:
    print(False)
else:
    print(True)
