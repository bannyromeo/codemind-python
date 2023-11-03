input_string = input()

# Convert the input string to lowercase for case insensitivity
input_string = input_string.lower()

# Create a set to store the unique alphabet characters
alphabet_set = set()

# Iterate through the string to check for alphabet characters
for char in input_string:
    if char.isalpha():
        alphabet_set.add(char)

# Check if the set contains all 26 alphabet characters
result = len(alphabet_set) == 26

print(result)
