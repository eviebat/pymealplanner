#!/usr/bin/python
# 
# title: userInput.py
# author: Emily VanDerveer
# purpose: This program asks for a user to enter 
# 0 or 1. If a 0 or 1 is not accepted, it repeats 
# until one is given.
import sys

def importUserSelection(userInput):
  try:
  	userInput = int(userInput);
  except ValueError:
    print "Invalid selection. Try again."
    return 2
  if userInput == 1:
    return userInput
  elif userInput == 0:
  	return userInput
  else:
  	print "Invalid selection. Try again."
  	return 2

def getUserSelection():
  input = sys.stdin.readline()
  choice = importUserSelection(input)

  while choice == 2:
    input = sys.stdin.readline()
    choice = importUserSelection(input)
  return choice