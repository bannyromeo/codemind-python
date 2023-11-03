s=input()
k=s.lower()
a=set()
for char in k:
    if char.isalpha():
        a.add(char)
if len(a)==len(s):
    print("True")
else:
    print("False")