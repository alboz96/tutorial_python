# Ask the user how many integers they want to input
num_integers = int(input("How many integers would you like to enter? "))

# Initialize an empty list to store the integers
lst = []

# Use a loop to take input for each integer
for i in range(num_integers):
    # Ask the user for each integer
    num = int(input("Enter integer " + str(i + 1) + ": "))
    # Append the integer to the list
    lst.append(num)

# Initialize a pointer for the next position of a non-zero element
non_zero_index = 0

# Traverse the list
for num in lst:
    if num != 0:
        lst[non_zero_index] = num  # Move the non-zero element to the correct position
        non_zero_index += 1

# After the loop, fill the rest of the list with zeros
while non_zero_index < len(lst):
    lst[non_zero_index] = 0
    non_zero_index += 1

# Print the resulting list
print(*lst)