sentences=[
    "a new world record was set",
    "in the holy city of ayodhya",
    "on the eve of diwali on tuesday",
    "with over three lakh diya or earthen lamps",
    "lit up simultaneously on the banks of sarayu river"
]
stopwords=['for','a','of','the','and','to','in','on','with','was']
res = [sub.split() for sub in sentences]
result=[]
for i in res:
    for j in i:
        if j in stopwords:
            continue
        result.append(j)
print(result)

#List Comprehension
print("By List Comprehension: ")
print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])

