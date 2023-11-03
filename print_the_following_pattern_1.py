# Input
N = int(input())

# Loop through each row
for i in range(N, 0, -1):
    # Loop through numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end='')
    print()  # Print a newline to move to the next row
