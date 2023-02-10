import os

for filename in os.listdir():
    if os.path.isfile(filename) or os.path.isdir(filename):
        print(filename)

file_name = input("Enter the file or directory name: ")
file_path = os.path.abspath(file_name)

if os.path.isfile(file_path):
    print("The directory of the file is:", os.path.dirname(file_path))
elif os.path.isdir(file_path):
    print("The directory of the directory is:", os.path.dirname(file_path))
else:
    print("File or directory not found.")