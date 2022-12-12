n=int(input())
sum=0
pro=n**2
temp=pro
while(pro!=0):
    r=pro%10
    sum=sum+r
    pro=pro//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")