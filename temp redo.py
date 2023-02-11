# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 01:57:15 2023

@author: jade annalise 
temp_converter remake using functions 
"""

#jade howlett 
#temperature converter remake 
#converts celcius to fahrenheit 
#converts fahrenheit to celcius 
#lets user choose the conversion and fills in text based on responses 

Running = True      #creates a variable that allows the converter to keep running without closing 

def celc_option(): #creates a function to take and hold the degrees in celcius, converts str to float and calculates conversion, holds conversion
    global celcius #creates global variable
    temp1 = float(input("Enter the temperature in Degrees " + store_choice + ": ")) #takes and stores user input in variable
    celcius = (temp1 * (9/5)) + 32 #uses input in variable temp1 to calculate temperature and stores in variable 
    
    
def fahr_option():      #creates a function to take and hold the degrees in celcius, converts str to float and calculates conversion, holds conversion
    global fahrenheit   #creates global variable
    temp2 = float(input("Enter the temperature in Degrees " + store_choice + ": ")) #takes and stores user input in variable
    fahrenheit = (temp2 - 32) * (5/9) #uses input in variable temp2 to calculate temperature and stores in variable 


def option():       #creates a function to take user input, fill in text, call functions in if statements 
    global store_choice         #creates global variable to hold the first unit of degrees 
    global secondary_txt        #creates global variable to hold the second unit of degrees 
    mode_choice = input("Please enter your selection: ")        #creates variable to take and hold user input, choice of conversion 
    if mode_choice.lower() == "a":      
         store_choice = "Celcius"       #sets variable as string celcius if user chooses option a 
         secondary_txt = "Fahrenheit"   #sets variable as string fahrenheit if user chooses option a 
         print("You have chosen to convert from " + store_choice + " to " + secondary_txt +".")  #prints the user's option choice based on variables
         celc_option()  #runs function celc_option
         print("The temperature is " + str(celcius) + " Degrees " + secondary_txt + ".")         #prints conversion answer and unit 
    elif mode_choice.lower() == "b": 
        store_choice = "Fahrenheit"     #sets variable as string fahrenheit if user chooses option b 
        secondary_txt = "Celcius"       #sets variable as string celcius if user chooses option b 
        print("You have chosen to convert from " + store_choice + " to " + secondary_txt +".") #prints the user's option choice based on variables
        fahr_option()
        print("The temperature is " + str(fahrenheit) + " Degrees " + secondary_txt + ".")     #prints conversion answer and unit 
    else: 
        print("Please choose a valid option.") #prints error message if user enters something other than a or b 

       
def main_option(): #creates function to keep the program running, allows user to choose to restart or exit, calls function option, prints welcome message and options message
    while Running == True: 
    
        print("Welcome to the temperature converter! Please choose from the following options: ")
        print("A. Celcius to Fahrenheit \nB. Fahrenheit to Celcius")
        option()
        
        Restart = False         #allows program to restart without closing
        while Restart == False: 
            choice = input("Would you like to restart?.(Y/N): ")
            if choice.lower() == "y":
                Restart = True #restarts the program 
            elif choice.lower() == "n":
                exit() #closes the program
            else:
                print("You must use Y or N.")

    
main_option() #calls function
   