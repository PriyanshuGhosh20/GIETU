tup=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_avg():
    avg=sum(tup)/len(tup)
    count=0
    for i in tup:
        if i>avg:
            count+=1
    return count*10
def sort_marks():
    return sorted(tup)
def frequency():
    freq=[]
    for x in range(26):
        count=0
        for y in sorted(tup):
            if x==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_avg())
print(frequency())
print(sort_marks()) 




