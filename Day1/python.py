print('Even:')
for i in range(2,101,2):
    print(i,end=' ')
print('\n\nOdd: ')
for i in range(1,101,2):
    print(i,end=' ')
print('\n\nReverse Odd: ')
for i in range(99,0,-2):
    print(i,end=' ')
print('\n\nReverse Even: ')
for i in range(100,0,-2):
    print(i,end=' ')
print('\n\nTill 50: ')
for i in range(1,101):
    if i==50:
        break
    print(i,end=' ')
else:
    print("\nElse for 'for' loop will print only if it will execute without any break statement.")
print("\n\nSkip 50: ")
for i in range(1,100):
    if i==50:
        continue
    print(i,end=' ')
print('\n\nPass: ')
for i in range(1,101):
    if i==50: #does nothing
        pass #null statement used to create an empty class
    print(i,end=' ')
print('\n\n ')

