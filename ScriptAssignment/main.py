# REQUIREMENTS:

# use the listdir() method from the OS module to iterate through all files within a specific directory.
# use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
# use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.
# print each file ending with a .”txt” file extension and its corresponding mtime to the console.


import os
import time

filePath = "files"

def openFile(file):
    """Open a file and print its contents to the console.

    Args:
        file (str): The full path to the file to be opened.
    """
    with open(file, "r") as f:
        data = f.read()
        print(data)
        f.close()


def readFiles(filePath):
    """Iterate through each file in the given directory and print its contents.

    For each entry in the directory, the build the full file path,
    check that the entry is a .txt file. For valid
    files, get the last modification time, convert to local time,
    and print before the displaying file's contents.

    Args:
        filePath (str): The relative or absolute path to the directory to scan.
    """
    for file in os.listdir(filePath):
        path = os.path.join(filePath, file)
        if os.path.isfile(path) and file.endswith(".txt"):
            modification_time = os.path.getmtime(path)
            local_time = time.ctime(modification_time)
            print("Last modification time(Local time):", local_time)
            openFile(path)


if __name__ == "__main__":
    readFiles(filePath)