n=int(input())
for i in range(n):
    s=input()
    m=s[::-1]
    if s==m and len(s)%2==0:
        print("YES","EVEN")
    elif s==m and len(s)%2!=0:
        print("YES","ODD")
    else:
        print("NO")

    