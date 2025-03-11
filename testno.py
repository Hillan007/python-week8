# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Input from user
number = float(input("Enter a number: "))

# Check the number and print the result
result = check_number(number)
print(result)
