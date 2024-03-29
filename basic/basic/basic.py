#!/usr/bin/env python

from __future__ import print_function  # convert print in function in python2, needs to be 1st line
import re
import sys
import random
import string
import time
from datetime import timedelta, datetime


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
try:
    MAX_INT = sys.maxint
except AttributeError:
    MAX_INT = sys.maxsize
MIN_INT = -MAX_INT - 1


def containsChars(string, search=re.compile(r'[^a-z0-9.]').search):
    """Example to understand regex. Default search returns true if string only contains a-z and 0-9."""
    return not bool(search(string))


def isAlphaNumeric(string):
    """Return True if string only contains numbers or letters."""
    return string.isalnum()


def isAlpha(string):
    """Return True if string only contains letters."""
    return string.isalpha()


def isAlphaUpper(string):
    """Return True if string only contains capital letters."""
    return string.isupper() and string.isalpha()


def isAlphaLower(string):
    """Return True if string only contains lower case letters."""
    return string.islower() and string.isalpha()


def isDigit(string):
    """Return True if string only contains digits."""
    return string.isdigit()


def charToASCII(character):
    """Return ASCII number of character."""
    return ord(character)


def ASCIIToChar(ascii):
    """Return character for ASCII value."""
    return chr(ascii)


def isInt(string):
    """Return True if string is an int."""
    try:
        int(string)
        return True
    except ValueError:
        return False


def isFloat(string):
    """Return True if string is a float."""
    try:
        float(string)
        return True
    except ValueError:
        return False


def intToBinary(n, padding=None):
    """Return number as binary. Variable padding adds 0s to the left of the number."""
    if padding is None:
        return "{:b}".format(n)
    return ("{:0" + str(padding) + "b}").format(n)


def binaryToInt(n):
    """Return binary string as int"""
    return int(n, 2)


def calculateFactors(n):
    """Calculate all divisors/factors of an integer n. e.g n=30, result={1,2,3,5,15}."""
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result


def greatestCommonDivisor(a, b):
    """Calculate the greatest common divisor of a and b.
    
    You should probably use: from fractions import gcd instead of this function, but
    here you can appreciate the beauty of the Euclidean algorithm
    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        (a, b) = b, a % b
    return a


def isPalindrome(n):
    """Return True if n is palindrome, False otherwise."""
    return n == n[::-1]


def isPalindromeHalf(n):
    """Returns True if n is palindrome, False otherwise.

    Should be faster in the worst case than IsPalindrome, as it checks only half the string.
    Empirically, the time taken is similar or worse.
    """
    length = len(n) // 2
    return n[:length] == n[-length:][::-1]


def isPowerOf2(n):
    """Return True if n is a power of 2 (like 2,4,8,16,32,64...1024) and False otherwise.

    Pretty cool, huh? I don't think I will use it often, but it has been coming up a lot
    lately so I thought I would include it. Warning, unknown behavior for negative numbers
    """
    return ((n & (n - 1)) == 0) and n != 0


def getTime():
    """Get current time. Not intended to know the current time, just to measure elapsed time."""
    # Check timeit to measure performance multiple times
    # e.g. timeit.timeit("[v for v in range(10000)]", number=10000)
    if sys.platform == "win32":
        # On Windows, the best timer is time.clock
        return time.clock()
    # On most other platforms the best timer is time.time
    return time.time()


def timeFunction(fn, *args):
    "Measure time that a function fn takes to execute and return."
    t = getTime()
    ret = fn(*args)
    return (getTime() - t, ret)


def getCurrentTime(time=True, date=False):
    """Get time (and date) in a human-readable format (yyyy-mm-dd hh:mm:ss)."""
    now = datetime.now()
    s = ""
    if date:
        s += "{} ".format(now.date())
    if time:
        s += "{:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second)
    return s.strip()


def getFormatedElapsedTime(t0, t1=None):
    """Get elapsed time between t0 and t1 in format hh:mm:ss:msmsms."""
    if t1 is None:
        t1 = getTime()  # time.clock() or time.time()
    return "{}".format(timedelta(seconds=t1-t0))


def getMaxIndex(myList):
    """Get index of max value in a list."""
    # For a faster implementation in big lists, try return numpy.argmax(myList)
    return myList.index(max(myList))


def getMinIndex(myList):
    """Get index of min value in a list."""
    # For a faster implementation in big lists, try return numpy.argmin(myList)
    return myList.index(min(myList))


def getMaxAndIndex(myList):
    """Get tuple (max, index) of max value in a list."""
    # For a faster implementation in big lists, try return numpy.argmax(myList)
    max_val = max(myList)
    return (max_val, myList.index(max_val))


def getMinAndIndex(myList):
    """Get tuple (min, index) of min value in a list."""
    # For a faster implementation in big lists, try return numpy.argmin(myList)
    min_val = min(myList)
    return (min_val, myList.index(min_val))


def orderList(seq):
    """Order a list, a string, or a tuple."""
    # For lists, list.sort() is faster but overwrites original list
    return sorted(seq)


def removeDuplicates(seq):
    """Remove repeated values from list, string, or tuple. Order will be lost. A list will be returned."""
    return list(set(seq))


def removeDuplicatesWithOrder(seq):
    """Remove repeated values from list, string, or tuple. Order will be kept. A list will be returned."""
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def duplicateAllElementsList(seq, num_reps=2):
    """Duplicate all elements of an array a number of times ([1, 2] becomes [1, 1, 2, 2])."""
    return [val for val in seq for _ in range(num_reps)]


def getRandomInt(minInt, maxInt=None):
    """Return the next random floating point number (int) in the range [0.0, 1.0)."""
    if maxInt is None:
        maxInt = minInt
        minInt = 0
    return random.randint(minInt, maxInt)


def getRandomFloat(minFloat, maxFloat):
    """Return a random floating point number N such that a<=N<=b for a<=b and b<=N<=a for b<a."""
    random.uniform(minFloat, maxFloat)


def getRandom():
    """Return the next random floating point number in the range [0.0, 1.0)."""
    return random.random()


def getRandomElementInList(seq):
    """Return random element from seq, which can be a string, list or tuple."""
    return random.choice(seq)


def getRandomChar(char_set="lowercase"):
    """Return a random character. char_set can be used to select the character domain."""
    if char_set == "letters":
        str = string.ascii_letters
    elif char_set == "lowercase":
        str = string.ascii_lowercase
    elif char_set == "uppercase":
        str = string.ascii_uppercase
    elif char_set == "digits":
        str = string.digits
    elif char_set == "letters_digits":
        str = string.ascii_letters + string.digits
    elif char_set == "all":
        str = string.ascii_letters + string.digits + string.punctuation
    else:
        str = string.ascii_lowercase
    return random.choice(str)


def mean(myList):
    """Calculate the average / mean value in a list of ints or floats."""
    return float(sum(myList)) / max(len(myList), 1)


def removeExtraSpaces(string):
    """Remove extra spaces of a string.

    @use removeExtraSpaces(" Hello   World     I am  Daniel  ")
    """
    return re.sub("\s+", " ", string).strip()


def printSeparator(character="-", length=64):
    """Print a long line of (the same) characters to see in a glance when something has happened.
    
    The length and character used can be configured with the parameters character and length

    @use printSeparator("*", lenght=10) --> prints **********
    """
    print(character * length)


def returnTableRow(widthCol, *columns, align="left"):
    """Return array in columns, aligned to the chosen side. Ready to be printed.
    
    @use returnTableRow(8, "Hello", "World", ["I", "am", "Daniel"], "Wow!", align="center")

    Use it to make a table:
        col_w, align = 10, "right"
        print(returnTableRow(col_w, "Animal", "Legs", align=align))
        print(returnTableRow(col_w, "ant", "6", align=align))
        print(returnTableRow(col_w, "octopus", "8", align=align))
        print(returnTableRow(col_w, "snake", "0", align=align))
    """
    if not isinstance(widthCol, int):
        print("ERROR: returnTableRow(widthCol, *columns, align=align)")
        return ""
    align = align.lower()
    if align == "left":
        cell = "{:<" + str(widthCol) + "}"
    elif align == "right":
        cell = "{:>" + str(widthCol) + "}"
    elif align == "center":
        cell = "{:^" + str(widthCol) + "}"
    else:
        print("ERROR: align can only take values: left, right, center")
        return ""
    buff = ""
    for col in columns:
        if isinstance(col, list) or isinstance(col, tuple):
            for ccol in col:
                buff += cell.format(ccol)
        else:
            buff += cell.format(col)
    return buff


def returnTableRowLeft(widthCol, *columns):
    """Return array in columns, aligned to the left. Ready to be printed.
    
    @use returnTableRowLeft(8, "Hello", "World", ["I", "am", "Daniel"], "Wow!")

    Use it to make a table:
        col_w = 10
        print(returnTableRowLeft(col_w, "Animal", "Legs"))
        print(returnTableRowLeft(col_w, "ant", "6"))
        print(returnTableRowLeft(col_w, "octopus", "8"))
        print(returnTableRowLeft(col_w, "snake", "0"))
    """
    return returnTableRow(widthCol, *columns, align="left")


def returnTableRowRight(widthCol, *columns):
    """Return array in columns, aligned to the right. Ready to be printed.
    
    @use returnTableRowRight(8, "Hello", "World", ["I", "am", "Daniel"])

    Use it to make a table:
        col_w = 10
        print(returnTableRowRight(col_w, "Animal", "Legs"))
        print(returnTableRowRight(col_w, "ant", "6"))
        print(returnTableRowRight(col_w, "octopus", "8"))
        print(returnTableRowRight(col_w, "snake", "0"))
    """
    return returnTableRow(widthCol, *columns, align="right")


def printNice(myList, print_result=True):
    """Print every element of an iterator in a different line, and subelements separated by spaces.

    @use printNice(("number", 1, "array", [1, 2, 3, 4, 5]))
    """
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
    if print_result:
        print(buff)
    return buff


def printNicer(myList, widthCol=None, side="left"):
    """Print every element of a list in a different line, and subelements in different columns. Good for matrices.

    Select width column or it will find optimal, and set side align (left, right)

    @use printNicer(["This is nice", [1,10,100], [20, 10, 0]])
    """
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
            buff += returnTableRowLeft(widthCol, el)
        else:
            buff += returnTableRowRight(widthCol, el)
    if print_result:
        print(buff)
    return buff


def indentString(s, indent="  "):
    """Add indent to the left of every line in a string.

    @use indentString("Hello\nDarkness\nMy\nOld\nFriend", indent="    ")
    """
    return indent + str(s).replace("\n", "\n" + indent)


def convertListToInt(myList):
    """Convert a list or a list of lists to integers. The original list will be overwritten.
    
    Good to convert a list where elements are strings containing numbers to integers.

    @use convertListToInt([["0", "1"], ["2"], "3"])
    """
    for i, el in enumerate(myList):
        if isinstance(el, list):
            for j, subel in enumerate(el):
                # We do this double cast to avoid errors and accept numbers like 1.55e8
                myList[i][j] = int(float(myList[i][j]))
        else:
            # We do this double cast to avoid errors and accept numbers like 1.55e8
            myList[i] = int(float(myList[i]))
    return myList


def convertListToFloat(myList):
    """Convert a list or a list of lists to floats. The original list will be overwritten.

    Good to convert a list where elements are strings containing numbers to floats.

    @use convertListToFloat([["0.3", "1.6"], ["2.9"], "4.2"])
    """
    for i, el in enumerate(myList):
        if isinstance(el, list):
            for j, subel in enumerate(el):
                myList[i][j] = float(myList[i][j])
        else:
            myList[i] = float(myList[i])
    return myList


def parseString(input, type=None):
    """Convert a string with elements separated by spaces and line-jumps to a list of lists.

    Every line will become a list of all its elements.
    If type is set to "int" or "float", all elements in the list will be casted to such type.
    
    Example:
        IN:  1 2 3\n4 5
        OUT: [[1, 2, 3], [4, 5]]
    
    @use parseString("3\n1 2 4\n2 2\n4 2 1\nhello world")
    """
    lines = input.split("\n")
    array = []
    [array.append(removeExtraSpaces(line).split()) for line in lines]
    if type is not None:
        if type == "int":
            convertListToInt(array)
        elif type == "float":
            convertListToFloat(array)
    return array


def readFile(filename, default="", print_input=False):
    """Return the file in filename as a string. If there is any problem, return default.

    @use readFile("my_file.txt", "Error while reading the file")
    """
    try:
        with open(filename, "r") as f:
            default = f.read()
        if print_input:
            print("File [{}] loaded:".format(filename))
    except IOError:
        if print_input:
            print("Error in filename, using default input:")
    if print_input:
        print(default)
    return default


def writeFile(filename, content, print_input=False, append=False):
    """Write content into filename and return True. If there is any problem, return False.
    
    If append is True, if the file exists content will be appended instead of overwritten.

    @use writeFile("my_file.txt", "Hello World", append=True)
    """
    try:
        op = "w+" if not append else "a+"
        with open(filename, op) as f:
            f.write(content)
        if print_input:
            if append:
                print("File [{}] appended".format(filename))
            else:
                print("File [{}] saved".format(filename))
    except IOError:
        if print_input:
            print("Error while creating / opening file [{}]".format(filename))
        return False
    return True


def readFileArgument(default_input="", print_input=False):
    """Return the content of a filename passed as an argument. If it fails, return default_input.

    The filename has to be the first argument passed (sys.argv[1]).

    @use readFileArgument("Error while reading the file")
    """
    if len(sys.argv) > 1:
        readFile(sys.argv[1], default_input, print_input)
    else:
        if print_input:
            print("No input file name argument, using default input:")
            print(default_input)
    return default_input


def readInputArguments(default_input="", print_input=False):
    """Return the arguments passed separated with spaces. If no arguments are passed, return default_input.

    @use readInputArguments("No arguments found", print_input=True)
    """
    if len(sys.argv) > 1:
        default_input = " ".join(sys.argv)
        if print_input:
            print("Arguments:")
    else:
        if print_input:
            print("No arguments, using default input:")
    if print_input:
        print(default_input)
    return default_input


def callProcess(process, cwd=None):
    """Call process, as if we were calling it from cmd. Use cwd to specify working directory.

    @use callProcess("ls -l -A", "my_relative_or_absolute_path")
    """
    cmd = process.split()
    p = subprocess.Popen(cmd, cwd=cwd)
    p.wait()


def askYNQuestion(question, message_on_failure=False):
    """Ask question and repeat it until the user responds yes or no. Return True (Y) or False (N)."""
    answer = ""
    while answer not in {"yes", "no", "y", "n"}:
        answer = input(question).lower()
    return answer[0] == "y"


"""
Profiling TIPS:

Profiling:
import cProfile
cProfile.run('mySlowFunction("test_value")')

Line Profiling: pip install line_profiler
Decorate the functions you want to profile with @profile (in line before def add @profile).
Run: kernprof -l script_to_profile.py
Run: python -m line_profiler script_to_profile.py.lprof
"""


if __name__ == "__main__":
    # example of how to use some of the functions together
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
    inp = readFileArgument(default, print_input=True)
    printSeparator()
    data = parseString(inp)
    printNicer(data)
    printSeparator()
    if askYNQuestion("Did you enjoy basic.py?\n>> "):
        print("You are awesome! :)")
    else:
        print("You are great! But you may want to reconsider your life choices... :S")
