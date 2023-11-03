# Read the input
n = int(input())
arr = list(map(int, input().split()))

# Initialize the last_odd_index to None
last_odd_index = None

# Iterate through the array from right to left
for i in range(n - 1, -1, -1):
    if arr[i] % 2 != 0:  # Check if the element is odd
        last_odd_index = i  # Update last_odd_index with the index of the last odd element
        break  # Exit the loop after finding the last odd element

# Display the last odd element index
print(last_odd_index)
