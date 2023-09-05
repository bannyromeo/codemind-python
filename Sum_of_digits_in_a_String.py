s=input()
m=0
for i in s:
    if i in "0123456789":
        m+=int(i)
print(m)