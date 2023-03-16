string=str(input())
if len(string)>=2:
    print(f'{string[0:2]}{string[-2:]}')
else:
    print(-1)
