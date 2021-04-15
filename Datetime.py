import subprocess as sp

import pynput
from pynput.keyboard import Key,Controller
keyboard = Controller()

import time

import random

import datetime

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# To see whats inside a specific module, print its directory
# The datetime module contais a 'date' class, a 'time' class, and a 'datetime'
print()
dir(datetime)
print("dir(datetime)")
print(Fore.MAGENTA + Style.BRIGHT + str(dir(datetime)))
print()

# Create a date
# To make a date you pass in 3 numbers: year-month-day
DOB = datetime.date(1977, 10, 8)
print(DOB)
print()
# You can access year, month, day seperately
print(DOB.year)
print(DOB.month)
print(DOB.day)
print()

# timedelta (a datetime class) lets you add or substract a number of days from a date
# & by printing the sum you can find the exact date after a number of days have passed 
DOB2 = datetime.date(2019, 4, 21)
DaysAfter = datetime.timedelta(300) # a positive number will increase the date
print(DOB2 + DaysAfter)
DaysBefore = datetime.timedelta(-300) # a negative number will decrease the date
print(DOB2 + DaysBefore)
print()

# By default dates are printed in this format: yyyy-mm-dd
print(DOB)
# You can specify a different format by creating a format code
# Lets display the full day-name, followed by the full month-name the day number, than the year
# 1st method, use the strftime method and pass the format string
# %A (full day)
# %B (full month) %d (day number)
# %Y (full year)
print(DOB.strftime("%A, %B %d, %Y"))
print()
# 2nd method, create a string with the format; insert format by starting with an open brace followed by a colon than close brace
message = "Guido Van Rossum was not born on {:%A, %B %d, %Y}."
print(Fore.WHITE+ Back.GREEN + Style.BRIGHT + str(message.format(DOB))) #pass the format and pass in the date, time or datetime object
print()

# Create objects using all 3 classes: 'date', 'datetime', and 'time' 
# I started my first repo on Feb 13, 2021 at 20:27 UTC
# 1) create a start_date object using the 'date' class with the 3 arguments: year, month, day
start_date = datetime.date(2021, 2, 13)
print(start_date)
# 2) create a start_time object using the 'time' class with the 3 arguments: hours, minutes, seconds
start_time = datetime.time(22, 55, 23)
print(start_time)
# 3) create a start_datetime object with both the date and time using the 'datetime' class with all arguments: year, month, day, hours, minutes, seconds
start_datetime = datetime.datetime(2021, 3, 13, 22, 55, 23)
print(start_datetime) 
print()


# name program to open
programname = "Notepad.exe"

# now open 
sp.Popen(programname)

time.sleep(1)
sentence = """This is a short tutorial on the 'Datetime' module in Python\n
\nKey Takeaways:
\n# To make a date you pass in 3 numbers: year-month-day
\n# You can access year, month, day seperately
\n# timedelta (a datetime class) lets you add or substract a number of days from a date
  & by printing the sum you can find the exact date after a number of days have passed
\n# By default dates are printed in this format: yyyy-mm-dd
\n# You can specify a different format by creating a format code
  1st method, use the strftime method and pass the format string
  2nd method, create a string with the format; insert format by starting with an open brace followed by a colon than close brace
\n\n-[S3]RGE"""

for c in sentence:
    keyboard.press(c)
    keyboard.release(c)
    delay = random.uniform(0,0.1)
    time.sleep(0.1)
print()
    
