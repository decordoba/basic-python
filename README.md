# basic-python
This repo consists of just one library / file (for now) called `basic.py`
This file contains some basic functions that perform tasks often used while coding in Python 2 or 3.
This includes some of the simple needs that I find myself writing over and over again
when solving algorithms in HackerRank or just coding in general. Instead of googling what
is the best way to do them every time, I have added them here so I can easily call them when I
need them. This saves a lot of time!

Every function comes with a comment on what it does and on how to use it, as well as other information.

Add the library to your python code using `from basic import *` or just use it as a general place to
look for some function when you don't recall how to do something simple, before searching for it somewhere else.
I am planning to increase the number of functions of this code as I find more useful things that should be added here.

## Functions and constants in the library
```python
MAX_INT
MIN_INT

def containsChars(string, search=re.compile(r'[^a-z0-9.]').search)
"""Example to understand regex. Default search returns true if string only contains a-z and 0-9."""


def isAlphaNumeric(string)
"""Return True if string only contains numbers or letters."""


def isAlpha(string)
"""Return True if string only contains letters."""


def isAlphaUpper(string)
"""Return True if string only contains capital letters."""


def isAlphaLower(string)
"""Return True if string only contains lower case letters."""


def charToASCII(character)
"""Return ASCII number of character."""


def ASCIIToChar(ascii)
"""Return character for ASCII value."""


def isInt(string)
"""Return True if string is an int."""


def isFloat(string)
"""Return True if string is a float."""


def calculateFactors(n)
"""Calculate all divisors/factors of an integer n. e.g n=30, result={1,2,3,5,15}."""


def greatestCommonDivisor(a, b)
"""Calculate the greatest common divisor of a and b.

You should probably use: from fractions import gcd instead of this function, but
here you can appreciate the beauty of the Euclidean algorithm
Unless b==0, the result will have the same sign as b (so that when
b is divided by it, the result comes out positive).
"""


def isPalindrome(n)
"""Return True if n is palindrome, False otherwise."""


def isPalindromeHalf(n)
"""Returns True if n is palindrome, False otherwise.
Should be faster in the worst case than IsPalindrome, as it checks only half the string.
Empirically, the time taken is similar or worse.
"""


def isPowerOf2(n)
"""Return True if n is a power of 2 (like 2,4,8,16,32,64...1024) and False otherwise.
Pretty cool, huh? I don't think I will use it often, but it has been coming up a lot
lately so I thought I would include it. Warning, unknown behavior for negative numbers
"""


def getTime()
"""Get current time. Not intended to know the current time, just to measure elapsed time."""


def timeFunction(fn, *args)
def getCurrentTime(time=True, date=False)
"""Get time (and date) in a human-readable format (yyyy-mm-dd hh:mm:ss)."""


def getFormatedElapsedTime(t0, t1=None)
"""Get elapsed time between t0 and t1 in format hh:mm:ss:msmsms."""


def transformCurvesToPlot(y_pts, x_pts)
"""Get a list of curves y_pts and x_pts and return a tuple formatted for pyplot.

pyplot can print more than one curve at the same time, but it doesn't do it in an intuitive way.
This method gets a list of curves y_pts
    [[curveA_y], [curveB_y], [curveC_y]]
and x_pts
    [[curveA_x], [curveB_x], [curveC_x]]
and returns a tuple
    ([[curveA_y0, curveB_y0, curveC_y0], [curveA_y1, curveB_y1, curveC_y1]...],
     [[curveA_x0, curveB_x0, curveC_x0], [curveA_x1, curveB_x1, curveC_x1]...])

It accepts curves of different lengths too. The returned y_pts and x_pts will plot all curves fine.

@use transformCurvesToPlot([[-2,2],[-2,-1,0,1,2],[0,0]], [[0,0],[-2,-1,0,1,2],[-2,2]])
@ret ([[-2, -2, 0], [2, -1, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 2, 0]],
      [[0, -2, -2], [0, -1, 2], [0, 0, 2], [0, 1, 2], [0, 2, 2], [0, 2, 2]])
"""


def plotLine(y_pts, x_pts=None, y_label=None, x_label=None, title=None, axis=None, style="-", color="", y_scale="linear", x_scale="linear", label=None, show=True)
"""Plot a line or point cloud.

It accepts several lines at the same time, if you set y_pts and x_pts as lists of lists.
@use plotLine([1,2,3,2,1], [0,1,2,3,4])
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


def plotLine1D(y_pts, y_label=None, x_label=None, title=None, y_scale="linear", label=None, show=True)
"""Print line between points in a list.

Every point will be separated a constant space in the x coordinates,
and the y coordinate of every point will be the values in the list.
"""


def plotLine2D(y_pts, x_pts, y_label=None, x_label=None, title=None, y_scale="linear", x_scale="linear", label=None, show=True)
"""Print line between points in a list. Every point is caracterized by an x and y coordinate."""


def plotCloud2D(y_pts, x_pts, y_label=None, x_label=None, title=None, style="x", y_scale="linear", x_scale="linear", label=None, show=True)
"""Print point cloud of coordinates (x_pts, y_pts)."""


def plotLegend(labels=None, location="best", boxed=None)
"""Display legend (labels can be set beforehand using other functions like plotLine) in location.
:param labels: labels shown. If None, all labels introduced in other functions will be displayed
:param location: "best", "upper right", "upper left", "lower left", "lower right", "right",
                 "center left", "center right", "lower center", "upper center", "center" (numbers 0 to 10)
:param boxed: whether to show a semi-transparent box around the legend or not. None means default
Find more (accurate location...) here: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
"""


def plotText(y, x, text, style="normal", color="k", fontsize=None, fontweight=None, verticalalignment="center", horizontalalignment="center", show=True)
"""Print text in the plot.
@use plotText(0.5, 0.5, "Middle") --> print text in the middle of screen
@use plotText(0.0, 0.0, "Bottom-Left") --> print text in the bottom left of screen
@use plotText(1.0, 1.0, "Top-Right") --> print text in the top right of screen
:param y: y coordinate for text (one int/float).
:param x: x coordinates for text (one int/float).
:param style: "normal", "italic" or "oblique"
:param color: 'r','g','b','c','m','y','k'...
:param fontsize: number of pixels or 'large', 'medium', 'smaller', 'small', 'x-large',
                 "xx-small", "larger", "x-small", "xx-large"
:param fontweight: "normal", "bold", "heavy", "light", "ultrabold", "ultralight"
:param verticalalignment: "center", "top", "bottom", "baseline"
:param horizontalalignment: "center", "right", "left"
:param show: whether to show result or not. Show is blocking (pauses the execution) until the
             plot window is closed
Find more (rotation, alpha, fontname, box...) here: https://matplotlib.org/users/text_props.html
"""


def getMaxIndex(myList)
"""Get index of max value in a list."""


def getMinIndex(myList)
"""Get index of min value in a list."""


def getMaxAndIndex(myList)
"""Get tuple (max, index) of max value in a list."""


def getMinAndIndex(myList)
"""Get tuple (min, index) of min value in a list."""


def orderList(seq)
"""Order a list, a string, or a tuple."""


def removeDuplicates(seq)
"""Remove repeated values from list, string, or tuple. Order will be lost. A list will be returned."""


def removeDuplicatesWithOrder(seq)
"""Remove repeated values from list, string, or tuple. Order will be kept. A list will be returned."""


def duplicateAllElementsList(seq, num_reps=2)
"""Duplicate all elements of an array a number of times ([1, 2] becomes [1, 1, 2, 2])."""


def getRandomInt(minInt, maxInt=None)
"""Return the next random floating point number (int) in the range [0.0, 1.0)."""


def getRandomFloat(minFloat, maxFloat)
"""Return a random floating point number N such that a<=N<=b for a<=b and b<=N<=a for b<a."""


def getRandom()
"""Return the next random floating point number in the range [0.0, 1.0)."""


def getRandomElementInList(seq)
"""Return random element from seq, which can be a string, list or tuple."""


def getRandomChar(char_set="lowercase")
"""Return a random character. char_set can be used to select the character domain."""


def mean(myList)
"""Calculate the average / mean value in a list of ints or floats."""


def removeExtraSpaces(string)
"""Remove extra spaces of a string.
@use removeExtraSpaces(" Hello   World     I am  Daniel  ")
"""


def printSeparator(character="-", length=64)
"""Print a long line of (the same) characters to see in a glance when something has happened.

The length and character used can be configured with the parameters character and length
@use printSeparator("*", lenght=10) --> prints **********
"""


def returnTableRow(widthCol, *columns, align="left")
"""Return array in columns, aligned to the chosen side. Ready to be printed.

@use returnTableRow(8, "Hello", "World", ["I", "am", "Daniel"], "Wow!", align="center")
Use it to make a table:
    col_w, align = 10, "right"
    print(returnTableRow(col_w, "Animal", "Legs", align=align))
    print(returnTableRow(col_w, "ant", "6", align=align))
    print(returnTableRow(col_w, "octopus", "8", align=align))
    print(returnTableRow(col_w, "snake", "0", align=align))
"""


def returnTableRowLeft(widthCol, *columns)
"""Return array in columns, aligned to the left. Ready to be printed.

@use returnTableRowLeft(8, "Hello", "World", ["I", "am", "Daniel"], "Wow!")
Use it to make a table:
    col_w = 10
    print(returnTableRowLeft(col_w, "Animal", "Legs"))
    print(returnTableRowLeft(col_w, "ant", "6"))
    print(returnTableRowLeft(col_w, "octopus", "8"))
    print(returnTableRowLeft(col_w, "snake", "0"))
"""


def returnTableRowRight(widthCol, *columns)
"""Return array in columns, aligned to the right. Ready to be printed.

@use returnTableRowRight(8, "Hello", "World", ["I", "am", "Daniel"])
Use it to make a table:
    col_w = 10
    print(returnTableRowRight(col_w, "Animal", "Legs"))
    print(returnTableRowRight(col_w, "ant", "6"))
    print(returnTableRowRight(col_w, "octopus", "8"))
    print(returnTableRowRight(col_w, "snake", "0"))
"""


def printNice(myList)
"""Print every element of an iterator in a different line, and subelements separated by spaces.
@use printNice(("number", 1, "array", [1, 2, 3, 4, 5]))
"""


def printNicer(myList, widthCol=None, side="left")
"""Print every element of a list in a different line, and subelements in different columns. Good for matrices.
Select width column or it will find optimal, and set side align (left, right)
@use printNicer(["This is nice", [1,10,100], [20, 10, 0]])
"""


def convertListToInt(myList)
"""Convert a list or a list of lists to integers. The original list will be overwritten.

Good to convert a list where elements are strings containing numbers to integers.
@use convertListToInt([["0", "1"], ["2"], "3"])
"""


def convertListToFloat(myList)
"""Convert a list or a list of lists to floats. The original list will be overwritten.
Good to convert a list where elements are strings containing numbers to floats.
@use convertListToFloat([["0.3", "1.6"], ["2.9"], "4.2"])
"""


def parseString(input, type=None)
"""Convert a string with elements separated by spaces and line-jumps to a list of lists.
Every line will become a list of all its elements.
If type is set to "int" or "float", all elements in the list will be casted to such type.

Example:
    IN:  1 2 3\n4 5
    OUT: [[1, 2, 3], [4, 5]]

@use parseString("3\n1 2 4\n2 2\n4 2 1\nhello world")
"""


def readFile(filename, default="", print_input=False)
"""Return the file in filename as a string. If there is any problem, return default.
@use readFile("my_file.txt", "Error while reading the file")
"""


def writeFile(filename, content, print_input=False, append=False)
"""Write content into filename and return True. If there is any problem, return False.

If append is True, if the file exists content will be appended instead of overwritten.
@use writeFile("my_file.txt", "Hello World", append=True)
"""


def readFileArgument(default_input="", print_input=False)
"""Return the content of a filename passed as an argument. If it fails, return default_input.
The filename has to be the first argument passed (sys.argv[1]).
@use readFileArgument("Error while reading the file")
"""


def readInputArguments(default_input="", print_input=False)
"""Return the arguments passed separated with spaces. If no arguments are passed, return default_input.
@use readInputArguments("No arguments found", print_input=True)
"""


def callProcess(process, cwd=None)
"""Call process, as if we were calling it from cmd. Use cwd to specify working directory.
@use callProcess("ls -l -A", "my_relative_or_absolute_path")
"""


def askYNQuestion(question, message_on_failure=False)
"""Ask question and repeat it until the user responds yes or no. Return True (Y) or False (N)."""


```
