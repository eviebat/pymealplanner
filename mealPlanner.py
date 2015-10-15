#!/usr/bin/python
#
#title: mealPlanner.pl
#author: Emily VanDerveer
#purpose: This program will assign a random meal from it's
# meal text to the daily meal slot.
import sys
from userInput import getUserSelection						#Only imports the used function from each module
from loadmeal import grabMeal

waitToStart = 1
name = raw_input('Please enter your name: ')

while (waitToStart):
  print "Welcome " + name + " \nPlease press 0 if you " \
  "are ready to begin"
  waitToStart = getUserSelection()


days = ['Sunday', 'Monday', 'Tuesday', 
'Wednesday','Thursday', 'Friday', 'Saturday'] 		    #List of days of the week
selector = 0

while selector == 0:
  f = open('thisWeeksMeal.txt', 'w') 					#Opens file for writing erasing anything 
  														# saved previously in file
  for day in days:										#Loops through each element in days list	
    breakfast = grabMeal('breakfast.txt')				#Loads breakfast element
    lunch = grabMeal('lunch.txt')						#Loads lunch element
    snack = grabMeal('snack.txt')						#Loads snack element
    dinner = grabMeal('dinner.txt')						#Loads dinner element
    menu = "\n" + day + " Menu:\n Breakfast - " \
    + breakfast + " Lunch - " + lunch + " Snack - " \
    + snack + " Dinner - " + dinner
    print menu
    f = open('thisWeeksMeal.txt', 'a')					
    f.write(menu)										#Writes menu variable to file for saving as
                        								# append so that each day will be saved and
                        								# not overrwritten.

  print "Press 1 if satisfied otherwise " \
  "enter 0 to try again."
  choice = getUserSelection()									#Calls getZeroOne method to accept only 0 or 1
  if choice == 1:
  	selector = 1							            #Allows for exit of while loop when user is satisfied


