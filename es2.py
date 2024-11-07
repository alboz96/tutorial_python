# Function to count vowels and consonants in a single line
def count_vowels_and_consonants(line):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_count = 0
    consonant_count = 0

    # Convert the line to lowercase for case-insensitive comparison
    line = line.lower()

    for char in line:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count


# Ask the user for the number of lines
num_lines = int(input("How many lines will there be? "))
# Initialize counters for the entire poem
total_vowels = 0
total_consonants = 0

# List to store the lines of the poem
lines = []

# Ask the user to enter the poem lines
print("Please enter the poem lines:")
for i in range(num_lines):
    line = input("Line " + str(i + 1) + ":").strip()
    lines.append(line)

# Read each line and calculate vowels and consonants
for i in range(num_lines):
    line = lines[i]
    vowels_in_line, consonants_in_line = count_vowels_and_consonants(line)

    total_vowels += vowels_in_line
    total_consonants += consonants_in_line

# Output the results
print("Number of vowels: ")
print(total_vowels)
print("Number of consonants: ")
print(total_consonants)