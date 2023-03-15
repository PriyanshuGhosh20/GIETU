dict1={
    "merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nyatt", "year":"ar"
    }
list1=["merry","christmas","and","happy","new","year"]
def trans(dict1,string):
    list2=[]
    for i in string:
        list2.append(dict1[i])
    return list2
print(list1)
print(trans(dict1,list1))
