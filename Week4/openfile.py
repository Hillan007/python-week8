try:
    # Open the file in read mode
    file = open("intro.py", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()