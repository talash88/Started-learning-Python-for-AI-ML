#Write  Python programs to print the contents of a directory using the os module. Search online for the function which does that

import os

path = "."

for root, dirs, files in os.walk(path):
    print("Folder:", root)

    for file in files:
        print("  File:", file)
