# Creates a function that gets users birth year from their age

from datetime import date;

age = int(input("What is your age? "));

def getBirthyear(age): 
    today = date.today() # Get today's date
    birthYear = today.year - age # Calculate year from age
    return birthYear 

print("Your birth year is " + str(getBirthyear(age)))




