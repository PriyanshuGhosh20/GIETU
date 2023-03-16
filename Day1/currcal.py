curr=str(input())
inr=int(input())
if curr=="EUR":
    print(0.01417*inr)
elif curr=="PND":
    print(0.0100*inr)
elif curr=="AUD":
    print(0.02140*inr)
elif curr=="CAD":
    print(0.02027*inr)
else:
    print(-1)
    
