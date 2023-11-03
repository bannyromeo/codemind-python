n = int(input())
l = list(map(int, input().split()))
a = []
d = []

# Iterate through the array and store the indices of all elements
for i in range(n):
    a.append(i)

# Iterate through the indices to find the indices of odd elements
for j in a:
    if l[j] % 2 == 0:
        d.append(j)

# Check if there are odd elements in the array
if d:
    print(max(d))
else:
    print(-1)  # In case there are no odd elements
