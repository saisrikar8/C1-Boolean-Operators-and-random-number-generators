'''
02/08/2021
Boolean Operators

-Used as conjunctions to combine and exclude keywords in a search 


A = True
B = False
C = 5 > 3 # True
D = 6 == 4 # False

if (A and B): #True and False >> False
  print("hello")

elif (C or D): #True or False >> True
  print("hi")

Truth Table:
  
    A      B      A and B.    A or B.  not A
  True   True      True       True    False
  True   False     False      True    False
  False  True      False      True    True
  False  False     False     False   True

print(5 == "five" or not(5 > 1 and not 0 != 0) or False and not 6 >= 6 and 10 <= 11)
print(5 == "five" or not(True and not False) or False and not 6 >= 6 and 10 <= 11)
print(False or not(True and not False) or False and not True and True)
print(False or False or False and False and True)
print(False or False or False and True)
print(False or False or False)
print(False or False)
print(False)

# Prompt the user to input a year
year = int(input("Please enter a year: "))
# Using if statements, output whether the inputted year is or is not a leap year

if (year % 100 == 0 and year % 400 == 0):
    print(str(year) + " is a leap year")

elif (year % 4 == 0 and year % 100 != 0):
    print(str(year) + " is a leap year")

else:
    print(str(year) + " is not a leap year")

===============================================================================================

Random Number Generator

A function that let the computeer pick a number within a range
import random

import random must be stated above any code 

formula:
  import random

  variable = random.randint(startNum, endNUm)


coin = random.randint(0,1)

if(coin == 0):
  print("heads")

elif(coin == 1):
  print("tails")

#Rolling a dice
import random

dice = random.randint(1,6)

print(dice)


#Excercise: Rock Paper Scissors (RPS)
import random


print("Welcome to RPS")
print("1. Rock\n2.Paper\n3.Scissors")
p1 = input("Enter your choice:\n")

cpu = random.randint(1,3)

if(p1 == "1" or p1 == "rock"):
  p1 = 1

elif(p1 == "2" or p1 == "paper"):
  p1 = 2

elif(p1 == "3" or p1 == "scissors"):
  p1 = 3

if(p1 == cpu):
  print("Tied")

elif(p1 == 1 and cpu == 3 or p1 == 2 and cpu == 1 or p1 == 3 and cpu == 2):
  print("You Won!")

elif(cpu == 1 and p1 == 3 or p1 == 2 and cpu == 1 or p1 == 3 and cpu == 2):
  print("You lost")

if(cpu == 1):
  print("cpu: rock")

elif(cpu == 2):
  print("cpu: paper")
elif(cpu == 3):
  print("cpu: scissors")
'''

