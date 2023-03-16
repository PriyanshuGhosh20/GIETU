dic={
    "P":"Pediatrics", "O":"Orthopedics", "E":"ENT"
}
list1="2,P,3,O,4,P"
def max_visit(list1,dic):
    P=list1.count('P')
    E=list1.count('E')
    O=list1.count('O')
    if P>E and P>O:
        spec=dic['P']
    elif E>0:
        spec=dic['E']
    else:
        spec=dic['O']
    return spec

spec=max_visit(list1,dic)
print(spec)
