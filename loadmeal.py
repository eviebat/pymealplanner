#!/usr/bin/python
#
#title: loadMeal.py
#author: Emily VanDerveer
#purpose: This program will open a file, read the
#text into a list and select on element from list
#randomly. 
import sys
import random

def grabMeal(filename):
  m = open(filename, 'r')               #Opens text file
  meals = m.readlines()					#Reads text into list held in memory
  meal = random.choice(meals)			#Randomly selects one element from list	
  return meal 							#Returns meal
  m.close()								#Closes text file