n=int(input())
fact=0
for i in range(1,n):
    if(n%i==0):
        fact=fact+i
if(fact>n):
    print("True")
else:
    print("False")