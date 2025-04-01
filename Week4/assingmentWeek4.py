# Ask the user for the filename
filename = input("Enter the filename to read: ")

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the content
        content = file.read()
        print("Original Content:")
        print(content)

    # Modify the content (e.g., convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
        print(f"\nModified content written to {new_filename}")

except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to read or write the file.")