#!/usr/bin/env python3

from basic.basic import removeExtraSpaces, writeFile


"""
This script automatized the update of the readme file when I change or add new functions
to basic.py
"""


if __name__ == "__main__":
    # Copy all lines from original README before any function is defined
    f = open("../README.md", "r")
    README = ""
    for line in f:
        if line.startswith("def "):
            break
        README += line
    f.close()

    # From basic.py copy all the function definitions as well as """...""" comments
    f = open("basic/basic.py", "r")
    save_line = False
    in_comment = False
    for line in f:
        if in_comment or line.startswith('    """'):
            if line.rstrip().endswith('"""'):
                in_comment = False
            elif line.startswith('    """'):
                in_comment = True
            README += line[4:]
            if not in_comment:
                README += "\n\n"
        elif save_line or line.startswith("def "):
            save_line = True
            sep = line.rfind("):")
            if sep < 0:
                README += removeExtraSpaces(line) + " "
                continue
            README += removeExtraSpaces(line[:sep]) + ")"
            README += "\n"
            save_line = False
    f.close()

    # Add this at the end of the file
    README += "```\n"

    # Overwrite README with updated functions
    writeFile("../README.md", README)
    print("README.md updated")
