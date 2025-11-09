# file management in python
y = lambda x: x*x
print(y)

import os

def create_file(file_name, content):
    """Create a new file and write content to it."""
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' created with content.")

def read_file(file_name):
    """Read content from a file."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def append_to_file(file_name, content):
    """Append content to an existing file."""
    with open(file_name, 'a') as file:
        file.write(content)
    print(f"Content appended to '{file_name}'.")

def delete_file(file_name):
    """Delete a file."""
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to delete '{file_name}'.")

def list_files(directory):
    """List all files in a directory."""
    try:
        files = os.listdir(directory)
        print("Files in directory:", files)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

if __name__ == "__main__":
    # Example usage
    file_name = "example.txt"
    
    # Create a file
    create_file(file_name, "Hello, world!\nThis is a test file.")

    # Read the file
    read_file(file_name)

    # Append to the file
    append_to_file(file_name, "\nAppending a new line.")

    # Read again to see the appended content
    read_file(file_name)

    # List files in the current directory
    list_files(".")

    # Delete the file
    delete_file(file_name)

    # Try to read the deleted file
    read_file(file_name)



# exceptoin handling


# fle management 
import os
path = ""
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("This is file")
    elif os.path.isdir(path):
        print("The path is directory")
else:
    print("That location does not exist")

# 
try:
    with open('') as file:
        print(file.read())
        print(file.closed())
except:
    print("The file is not found")


# writnig a file in pthon
text = "this is some text"
with open ('test.txt', 'w') as file:
    file.write(text)
# to append osme text file
with open('text.txt', 'a') as file:
    file.write(text)


# to copy a file
# copyfile() - copies the contents of a file
# copy() - copyfile()+permission mode + destination can be a deirectory
# copy2() - copy() + copies meta data
# the arguments are exactly the same but with defferent functionalities
import shutil
try:
    shutil.copyfile('filename', 'destination path')
    shutil.copy('filename', 'destination path')
    shutil.copy2('filename', 'destination path')
except FileNotFoundError:
    print("The file is not found") 

# how to move a file
import os
source = "folder"
destination = ""

try:
    if os.path.exists(destination):
        print("There is already a file in the directory")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

# how to remove a file from a directory
path = "empty folder"

try:
    os.remove(path)
except FileNotFoundError:
    print("the file is not found")
except PermissionError:
    print("you don't have permission to remove the file")