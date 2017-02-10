#!/usr/bin/env

import re
import sys
import random

"""
@author: Daniel de Cordoba Gil
@github: https://github.com/decordoba

This file contains some basic functions that perform some tasks used often in Python.
This includes some of the simple needs that I find myself writing over and over again
when solving algorithms in HackerRank or just coding in general. Instead of googling what
is the way to do them every time, I have added them here so I can easily call them when I
need them. This saves a lot of time of searching the Internet
"""

# Useful constants, the maximum and minimum possible integer
# Python can treat bigger numbers, which are then trated as long integers.
# If you may be using values higher than 2147483647 or lower than -2147483648,
# these numbers may not work, consider using constants like 2**127 or 10**100
MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1

# Example to understand regex. By now it returns true if string only contains a-z and 0-9
def containsChars(string, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(string))

# Return True if string only contains numbers or letters
def isAlphaNumeric(string):
    return string.isalnum()

# Return True if string only contains letters
def isAlpha(string):
    return string.isalpha()

# Return True if string only contains capital letters
def isAlphaUpper(string):
    return string.isupper() and string.isalpha()

# Return True if string only contains lower case letters
def isAlphaLower(string):
    return string.islower() and string.isalpha()

# Return ASCII number of character
def charToASCII(character):
    return ord(character)

# Return character for ASCII value
def ASCIIToChar(ascii):
    return chr(ascii)

# Return True if string is an int
def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# Return True if string is a float
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Calculate all divisors/factors of an integer n. e.g n=30, result={1,2,3,5,15}
def calculateFactors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

# Get index of max value in a list
def getMaxIndex(myList):
    # For a faster implementation in big lists, try return numpy.argmax(myList)
    return myList.index(max(myList))

# Get index of min value in a list
def getMinIndex(myList):
    # For a faster implementation in big lists, try return numpy.argmin(myList)
    return myList.index(min(myList))

# Get tuple (max, index) of max value in a list
def getMaxAndIndex(myList):
    # For a faster implementation in big lists, try return numpy.argmax(myList)
    max_val = max(myList)
    return (max_val, myList.index(max_val))

# Get tuple (min, index) of min value in a list
def getMinAndIndex(myList):
    # For a faster implementation in big lists, try return numpy.argmin(myList)
    min_val = min(myList)
    return (min_val, myList.index(min_val))

# Order a list, a string, or a tuple
def orderList(seq):
    # For lists, list.sort() is faster but overwrites original list
    return sorted(seq)

# Remove repeated values from list, string, or tuple. Order will be lost. A list will be returned
def removeDuplicates(seq):
    return list(set(seq))

# Remove repeated values from list, string, or tuple. Order will be kept. A list will be returned
def removeDuplicatesWithOrder(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

# Return the next random floating point number (int) in the range [0.0, 1.0)
def getRandomInt(minInt, maxInt):
    return random.randint(minInt, maxInt)

# Return a random floating point number N such that a<=N<=b for a<=b and b<=N<=a for b<a
def getRandomFloat(minFloat, maxFloat):
    random.uniform(minFloat, maxFloat)

# Return the next random floating point number in the range [0.0, 1.0)
def getRandom():
    return random.random()

# Calculate the average / mean value in a list of ints or floats
def mean(myList):
    return float(sum(myList)) / max(len(myList), 1)

# Removes extra spaces of a string
# @use removeExtraSpaces(" Hello   World     I am  Daniel  ")
def removeExtraSpaces(string):
    return re.sub('\s+', ' ', string).strip()

# Prints a long line of characters to see in a glance when something has happened. The length and
# character used can be configured with the parameters character and length
# @use printSeparator("*")
def printSeparator(character="-", length=64):
    print character*length

# Prints array in columns, aligned to the left
# @use printLikeTableRowLeft(8, "Hello", "World", ["I", "am", "Daniel"])
def printLikeTableRowLeft(widthCol, *columns):
    if not isinstance(widthCol, int):
        print "ERROR: printLikeTableRowLeft(widthCol, *columns)"
    else:
        cell = "{:<" + str(widthCol) + "}"
        buff = ""
        for col in columns:
            if isinstance(col, list) or isinstance(col, tuple):
                for ccol in col:
                    buff += cell.format(ccol)
            else:
                buff += cell.format(col)
        print buff

# Prints array in columns, aligned to the right
# @use printLikeTableRowRight(8, "Hello", "World", ["I", "am", "Daniel"])
def printLikeTableRowRight(widthCol, *columns):
    if not isinstance(widthCol, int):
        print "ERROR: printLikeTableRowRight(widthCol, *columns)"
    else:
        cell = "{:>" + str(widthCol) + "}"
        buff = ""
        for col in columns:
            if isinstance(col, list) or isinstance(col, tuple):
                for ccol in col:
                    buff += cell.format(ccol)
            else:
                buff += cell.format(col)
        print buff

# Prints every element of an iterator in a different line, and subelements separated by spaces
# @use printNice(("number", 1, "array", [1,2,3,4,5]))
def printNice(myList):
    buff = ""
    for el in myList:
        if isinstance(el, list) or isinstance(el, tuple):
            for i, subel in enumerate(el):
                if i != len(el) - 1:
                    buff += str(subel) + " "
                else:
                    buff += str(subel)
        else:
            buff += str(el)
        buff += "\n"
    print buff

# Prints every element of a list in a different line, and subelements in different columns
# Select width column or it will find optimal, and set side align (left, right)
# @use printNicer(["This is nice", [1,10,100], [20, 10, 0]])
def printNicer(myList, widthCol=None, side="left"):
    if widthCol is None:
        widthCol = 0
        for el in myList:
            if isinstance(el, list) or isinstance(el, tuple):
                for subel in el:
                    widthCol = max(widthCol, len(str(subel)))
        widthCol += 2
    buff = ""
    for el in myList:
        if side == "left":
            printLikeTableRowLeft(widthCol, el)
        else:
            printLikeTableRowRight(widthCol, el)

# Converts a list or a list of lists to integers. Attention, the original list will be overwritten
# @use convertListToInt([["0", "1"], ["2"], "3"])
def convertListToInt(myList):
    for i, el in enumerate(myList):
        if isinstance(el, list):
            for j, subel in enumerate(el):
                myList[i][j] = int(myList[i][j])
        else:
            myList[i] = int(myList[i])
    return myList

# Converts a list or a list of lists to floats. Attention, the original list will be overwritten
# @use convertListToFloat([["0.3", "1.6"], ["2.9"], "4.2"])
def convertListToFloat(myList):
    for i, el in enumerate(myList):
        if isinstance(el, list):
            for j, subel in enumerate(el):
                myList[i][j] = float(myList[i][j])
        else:
            myList[i] = float(myList[i])
    return myList

# Gets a string with elements separated by spaces and line-jumps and returns as a list of lists,
# where every line becomes a list of all its elements. e.g. 1 2 3\n4 5 becomes [[1, 2, 3], [4, 5]]
# If type is set to "int" or "float", all elements in the list will be casted to such type
# @use parseString("3\n1 2 4\n2 2\n4 2 1\nhello world")
def parseString(input, type=None):
    lines = input.split('\n')
    array = []
    [array.append(removeExtraSpaces(line).split()) for line in lines]
    if type is not None:
        if type == "int":
            convertListToInt(array)
        elif type == "float":
            convertListToFloat(array)
    return array

# Tries to return the content of a filename passed as an argument. If it fails, it returns input
# @use readFileArgument("Error while reading the file")
def readFileArgument(input="", print_input=False):
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                input = f.read()
            if print_input:
                print "Input file loaded:"
        except IOError:
            if print_input:
                print "Error in input file name, using default input:"
    else:
        if print_input:
            print "No input file name argument, using default input:"
    if print_input:
        print input
    return input

# Returns the arguments passed separated with spaces. If no arguments are passed, it returns input
# @use readInputArguments("No arguments found", print_input=True)
def readInputArguments(input="", print_input=False):
    if len(sys.argv) > 1:
        input = sys.argv[1]
        for arg in sys.argv[2:]:
            input += " " + arg
        if print_input:
            print "Arguments:"
    else:
        if print_input:
            print "No arguments, using default input:"
    if print_input:
        print input
    return input

"""
if __name__ == "__main__":

    default = '''89 42 0 2 24 20 40 37 30 77
66 75 9 59 69 66 52 14 85 36
82 68 0 81 36 25 48 53 11 68
6 96 82 53 17 70 26 12 91 82
34 86 22 18 66 73 82 88 18 36
90 43 43 93 80 96 12 28 74 93
19 75 30 48 31 76 84 29 20 15
29 73 88 9 36 40 40 19 1 45
77 31 6 68 36 40 22 43 27 61
70 21 2 89 30 91 66 74 79 92'''
    input = readFileArgument(default, print_input=True)
    printSeparator()
    data = parseFile(input)
    printNicer(data)
    printSeparator()
"""