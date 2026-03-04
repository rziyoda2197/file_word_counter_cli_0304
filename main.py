filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()

    words = text.split()
    print("Word count:", len(words))

except FileNotFoundError:
    print("File not found.")
