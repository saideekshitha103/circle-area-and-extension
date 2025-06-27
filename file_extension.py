# Program to get the file extension
filename = input("Input the filename: ")

# Split the filename at the last dot and get the extension
extension = filename.split(".")[-1]

print(f"The extension of the file is : {extension}")
