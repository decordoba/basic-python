# basic-python
This repo consists of just one library / file (for now) called `basic.py`
This file contains some basic functions that perform tasks often used while coding in Python 2.7.
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

def isAlphaNumeric(string)

def isAlpha(string)

def isAlphaUpper(string)

def isAlphaLower(string)

def charToASCII(character)

def ASCIIToChar(ascii)

def isInt(string)

def isFloat(string)

def calculateFactors(n)

def getMaxIndex(myList)

def getMinIndex(myList)

def getMaxAndIndex(myList)

def getMinAndIndex(myList)

def orderList(seq)

def removeDuplicates(seq)

def removeDuplicatesWithOrder(seq)

def getRandomInt(minInt, maxInt)

def getRandomFloat(minFloat, maxFloat)

def getRandom()

def mean(myList)

def removeExtraSpaces(string)

def printSeparator(character="-", length=64)

def printLikeTableRowLeft(widthCol, *columns)

def printLikeTableRowRight(widthCol, *columns)

def printNice(myList)

def printNicer(myList, widthCol=None, side="left")

def convertListToInt(myList)

def convertListToFloat(myList)

def parseString(input, type=None)

def readFileArgument(input="", print_input=False)

def readInputArguments(input="", print_input=False)
```
