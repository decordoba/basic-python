#!/usr/bin/env

import re
import sys
import random
import time
import matplotlib.pyplot as plt

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

# Calculate the greatest common divisor of a and b
def greatestCommonDivisor(a, b):
    # You should probably use from fractions import gcd instead of this function, but
    # here you can appreciate the beauty of the Euclidean algorithm
    # Unless b==0, the result will have the same sign as b (so that when
    # b is divided by it, the result comes out positive).
    while b:
        (a, b) = b, a % b
    return a

# Returns True if n is palindrome, False otherwise
def isPalindrome(n):
    return n == n[::-1]

# Returns True if n is palindrome, False otherwise. Should be faster in the worst case, as it
# checks only half the string. Empirically, the time taken is similar or worse
def isPalindromeFalf(n):
    l = len(n) // 2
    return n[:l] == n[-l:][::-1]

# Returns True if n is a power of 2 (like 2,4,8,16,32,64...1024) and False otherwise
def isPowerOf2(n):
    # Pretty cool, huh? I don't think I will use it often, but it has been coming up a lot
    # lately so I thought I would include it. Warning, unknown behavior for negative numbers
    return ((n & (n - 1)) == 0) and n != 0

# Get current time. Not intended to know the current time, just to measure elapsed time
def getTime():
    # Check timeit to measure performance multiple times
    # e.g. timeit.timeit('[v for v in range(10000)]', number=10000)
    if sys.platform == 'win32':
        # On Windows, the best timer is time.clock
        return time.clock()
    # On most other platforms the best timer is time.time
    return time.time()

# pyplot can print more than one curve at the same time, but it doesn't do it in an intuitive way.
# transformCurvesToPlot gets a list of  curves y_pts = [[curveA_y], [curveB_y], [curveC_y]] and
# x_pts = [[curveA_x], [curveB_x], [curveC_x]] and returns a tuple like:
# ([[curveA_y0, curveB_y0, curveC_y0], [curveA_y1, curveB_y1, curveC_y1]...]],
# [curveA_x0, curveB_x0, curveC_x0], [curveA_x1, curveB_x1, curveC_x1]...])
# It accepts curves of different lengths too. The new y_pts and x_pts will plot all curves ok.
#@use transformCurvesToPlot([[-2,2],[-2,-1,0,1,2],[0,0]], [[0,0],[-2,-1,0,1,2],[-2,2]])
def transformCurvesToPlot(y_pts, x_pts):
    new_y_pts = []
    new_x_pts = []
    last_row = max([len(row) for row in y_pts])
    for i, row in enumerate(y_pts):
        for j, y in enumerate(row):
            try:
                new_y_pts[j].append(y)
                new_x_pts[j].append(x_pts[i][j])
            except IndexError:
                new_y_pts.append([y])
                new_x_pts.append([x_pts[i][j]])
        x = x_pts[i][j]
        while j < last_row:
            j += 1
            try:
                new_y_pts[j].append(y)
                new_x_pts[j].append(x)
            except IndexError:
                new_y_pts.append([y])
                new_x_pts.append([x])
    return (new_y_pts, new_x_pts)


# Plot a line or point cloud. Also accepts several lines at the same time, if you set y_pts and
# x_pts as lists of lists.
#@use transformCurvesToPlot([[-2,2],[-2,-1,0,1,2],[0,0]], [[0,0],[-2,-1,0,1,2],[-2,2]])
def plotLine(y_pts, x_pts=None, y_label=None, x_label=None, title=None, axis=None, style="-",
             color="", y_scale="linear", x_scale="linear", label=None, show=True):
    """
    :param y_pts: y coordinates. A list of list can represent several lines
    :param x_pts: x coordinates. A list of list can represent several lines
    :param y_label: label for y axis
    :param x_label: label for x axis
    :param title: the title of the figure
    :param axis: len4 list [xmin, xmax, ymin, ymax] to pick range we will see
    :param style: ('-': line), ('x': cross), ('o': circle), ('s': squre), ('--': dotted line)...
    :param color: 'r','g','b','c','m','y','k'... If left blank, every curve will take a new color
    :param label: text that will be displayed if we show a legend
    :param show: whether to show result or not. Show is blocking (pauses the execution) until the
                 plot window is closed
    """
    if x_pts is None:
        plt.plot(y_pts, color + style, label=label)
    else:
        if isinstance(y_pts, list) and isinstance(y_pts[0], list):
            (y_pts, x_pts) = transformCurvesToPlot(y_pts, x_pts)
        plt.plot(x_pts, y_pts, color + style, label=label)
    if y_label is not None:
        plt.ylabel(y_label)
    if x_label is not None:
        plt.xlabel(x_label)
    if title is not None:
        plt.title(title)
    if axis is not None:
        plt.axis(axis)
    plt.yscale(y_scale)
    plt.xscale(x_scale)
    plt.draw()
    if show:
        plt.show()

# Print line between points in a list. Every point will be separated a constant space in the
# x coordinates, and the y coordinate of every point will be the values in the list
def plotLine1D(y_pts, y_label=None, x_label=None, title=None, y_scale="linear", label=None,
               show=True):
    plotLine(y_pts, y_label=y_label, x_label=x_label, title=title, y_scale=y_scale, label=label,
             show=show)

# Print line between points in a list. Every point is caracterized by and x and y coordinate
def plotLine2D(y_pts, x_pts, y_label=None, x_label=None, title=None, y_scale="linear",
               x_scale="linear", label=None, show=True):
    plotLine(y_pts, x_pts=x_pts, y_label=y_label, x_label=x_label, title=title, y_scale=y_scale,
             x_scale=x_scale, label=label, show=show)

# Print point cloud of coordinates (x_pts, y_pts)
def plotCloud2D(y_pts, x_pts, y_label=None, x_label=None, title=None, style='x', y_scale="linear",
                x_scale="linear", label=None, show=True):
    plotLine(y_pts, x_pts=x_pts, y_label=y_label, x_label=x_label, title=title, style=style,
             y_scale=y_scale, x_scale=x_scale, label=label, show=show)

# Print text in the plot
def plotText(y, x, text, style="normal", color="k", fontsize=None, fontweight=None,
             verticalalignment="center", horizontalalignment="center", show=True):
    """
    :param y: y coordinate for text (one int/float).
    :param x: x coordinates for text (one int/float).
    :param style: 'normal', 'italic' or 'oblique'
    :param color: 'r','g','b','c','m','y','k'...
    :param fontsize: number of pixels or 'large', 'medium', 'smaller', 'small', 'x-large',
                     'xx-small', 'larger', 'x-small', 'xx-large'
    :param fontweight: 'normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight'
    :param verticalalignment: 'center', 'top', 'bottom', 'baseline'
    :param horizontalalignment: 'center', 'right', 'left'
    :param show: whether to show result or not. Show is blocking (pauses the execution) until the
                 plot window is closed
    Find more (rotation, alpha, fontname, box...) here: https://matplotlib.org/users/text_props.html
    """
    plt.text(x, y, text, style=style, color=color, fontsize=fontsize, fontweight=fontweight,
             verticalalignment=verticalalignment, horizontalalignment=horizontalalignment)
    plt.draw()
    if show:
        plt.show()

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
def getRandomInt(minInt, maxInt=None):
    if maxInt is None:
        maxInt = minInt
        minInt = 0
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

# Returns array in columns, aligned to the left. Ready to be printed
# @use returnTableRowLeft(8, "Hello", "World", ["I", "am", "Daniel"])
def returnTableRowLeft(widthCol, *columns):
    if not isinstance(widthCol, int):
        print "ERROR: returnTableRowLeft(widthCol, *columns)"
    else:
        cell = "{:<" + str(widthCol) + "}"
        buff = ""
        for col in columns:
            if isinstance(col, list) or isinstance(col, tuple):
                for ccol in col:
                    buff += cell.format(ccol)
            else:
                buff += cell.format(col)
        return buff
    return ""

# Return array in columns, aligned to the right. Ready to be printed
# @use returnTableRowRight(8, "Hello", "World", ["I", "am", "Daniel"])
def returnTableRowRight(widthCol, *columns):
    if not isinstance(widthCol, int):
        print "ERROR: returnTableRowRight(widthCol, *columns)"
    else:
        cell = "{:>" + str(widthCol) + "}"
        buff = ""
        for col in columns:
            if isinstance(col, list) or isinstance(col, tuple):
                for ccol in col:
                    buff += cell.format(ccol)
            else:
                buff += cell.format(col)
        return buff
    return ""

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
            print returnTableRowLeft(widthCol, el)
        else:
            print returnTableRowRight(widthCol, el)

# Converts a list or a list of lists to integers. Attention, the original list will be overwritten
# @use convertListToInt([["0", "1"], ["2"], "3"])
def convertListToInt(myList):
    for i, el in enumerate(myList):
        if isinstance(el, list):
            for j, subel in enumerate(el):
                # We do this double cast to avoid errors and accept numbers like 1.55e8
                myList[i][j] = int(float(myList[i][j]))
        else:
            # We do this double cast to avoid errors and accept numbers like 1.55e8
            myList[i] = int(float(myList[i]))
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

# Returns the file in filename as a string. If there is any problem, returns default
# @use readFile("my_file.txt", "Error while reading the file")
def readFile(filename, default="", print_input=False):
    try:
        with open(filename, 'r') as f:
            default = f.read()
        if print_input:
            print "File [{}] loaded:".format(filename)
    except IOError:
        if print_input:
            print "Error in filename, using default input:"
    if print_input:
        print default
    return default

# Writes the string content in the file filename and returns True. If there is any problem,
# returns False. If append is set to True, in case the file exists it will append the content
# instead of overwriting it.
# @use writeFile("my_file.txt", "Hello World", append=True)
def writeFile(filename, content, print_input=False, append=False):
    try:
        op = "w+"
        if append: op = "a+"
        with open(filename, op) as f:
            f.write(content)
        if print_input:
            if append:
                print "File [{}] appended".format(filename)
            else:
                print "File [{}] saved".format(filename)
    except IOError:
        if print_input:
            print "Error while creating / opening file [{}]".format(filename)
        return False
    return True

# Tries to return the content of a filename passed as an argument. If it fails, it returns input
# @use readFileArgument("Error while reading the file")
def readFileArgument(input="", print_input=False):
    if len(sys.argv) > 1:
        readFile(sys.argv[1], input, print_input)
    else:
        if print_input:
            print "No input file name argument, using default input:"
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

# Call process, as if we were calling it from cmd. Use cwd to specify current working dir.
# @use callProcess("ls -l -A", "my_relative_or_absolute_path")
def callProcess(process, cwd=None):
    cmd = process.split()
    p = subprocess.Popen(cmd, cwd=cwd)
    p.wait()

# Ask question and repeat it until the user responds yes or no
def askYNQuestion(question):
    answer = ""
    while answer not in {"yes", "no", "y", "n"}:
        answer = raw_input(question).lower()
    return answer[0] == "y"

"""
TIPS:

Profiling:
import cProfile
cProfile.run('mySlowFunction("test_value")')

Line Profiling: pip install line_profiler
Decorate the functions you want to profile with @profile (in line before def add @profile).
Run: kernprof -l script_to_profile.py
Run: python -m line_profiler script_to_profile.py.lprof
"""

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