n = int(input())
for _ in range(n):
    a = input()
    k = a.split()
    found_digit = False
    for word in k:
        if any(char.isdigit() for char in word):
            found_digit = True
            break
    if found_digit:
        print("Yes")
    else:
        print("No")
