s=input()
t = 0
for i in s:
    if i in "123456789":
        t+=int(i)
print(t)