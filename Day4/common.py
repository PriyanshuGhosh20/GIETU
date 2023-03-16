str1="I like Python"
str2="Java is a very popular language"
res=""
for i in str1:
    if i in str2 and i!=" ":
        res=res+i
print(res)
