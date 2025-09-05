"""Task 2: Write and Append Data to a File
 Problem Statement:Write a Python program that:
  1. Takes user input and writes it to a file named output.txt.
   2. Appends additional data to the same file.
   3. Reads and displays the final content of the file."""


user_input = input("Enter text:")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

Add_data = input("Enter Add_data:")
with open("output.txt", "a") as file:
    file.write(Add_data + "\n")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)