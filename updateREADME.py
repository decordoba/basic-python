#!/usr/bin/env

from basic import *

"""
This script automatized the update of the readme file when I change or add new functions
to basic.py
"""

if __name__ == "__main__":
    # Copy all lines from original README before any function is defined
    f = open("README.md", "r")
    README = ""
    for line in f:
        if line.startswith("def "):
            break
        README += line
    f.close()

    # From basic.py copy all the function definitions
    f = open("basic.py", "r")
    for line in f:
        if line.startswith("def "):
            README += removeExtraSpaces(line)[:line.rfind(":")] + "\n\n"
    f.close()

    # Add this at the end of the file
    README += "```\n"

    # Overwrite README with updated functions
    writeFile("README.md", README)
    print "README.md updated"
