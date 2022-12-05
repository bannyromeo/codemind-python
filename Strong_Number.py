n=int(input())
temp=n
sum=0
while(n>0):
    i=1
    fact=1
    r=n%10
    while(i<=r):
        fact=fact*i
        i+=1
    sum+=fact
    n=n//10
if(temp==sum):
    print("The number",temp,"is a strong number",)
else:
    print("The number",temp,"is not a strong number",)