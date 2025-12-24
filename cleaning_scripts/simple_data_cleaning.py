print("--------------------This is a data cleaning python code--------------------\n")
user_input = input("Enter names separated by commas: ")

# Split input into a list and remove extra spaces
data = [name.strip() for name in user_input.split(",")]

# Clean the names
cleaned_names = [
    ''.join(char for char in name if char.isalpha()).capitalize() 
    for name in data
]

# Count names that had numbers
names_with_numbers = sum(any(char.isdigit() for char in name) for name in data)

print("Cleaned Names:", cleaned_names)
print(f"The names that had numbers are {names_with_numbers}")
