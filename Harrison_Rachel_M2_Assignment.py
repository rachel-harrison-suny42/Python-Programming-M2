#Rachel Harrison - CSCI-3025-01 - Python Programming
#M2 Assignment - Variables, Data Types, and Expressions

##################################
#Numeric Data Types and Arithmetic
##################################

##floats vs. decimals##

print("\nLets's add 0.3 and 0.6.  First we will them as type(float) and then repeat the operation using Decimal().")

#floats# - seems like it should give exact decimals, but it doesn't

floatOne = 0.3  #NUMERIC VARIABLE REQUIREMENT 1/3
floatTwo = 0.6  #NUMERIC VARIABLE REQUIREMENT 2/3

print(f"\nSum when adding 0.3 and 0.6 as floats: {floatOne + floatTwo}")  #NUMERIC OPERATION REQUIREMENT 1/1

#we expect the result to be 0.9, but it is not!
print("\n vs.")
#decimals# - actually does treat decimals and decimal arithmetic as we expect

from decimal import Decimal

decOne = Decimal('0.3')  #NUMERIC VARIABLE REQUIREMENT 3/3
decTwo = Decimal('0.6')  #NUMERIC VARIABLE REQUIREMENT 4/3

sum = decOne + decTwo #NUMERIC OPERATION REQUIREMENT 2/1
print(f"\nSum when adding 0.3 and 0.6 as decimals(): {sum}\n")  #STRING FORMATTING REQUIREMENT 1/1

print("You think to yourself, maybe this is just a quirk of the print function, and these sums are actually equal in their internal systems states.  Ok, well let's test that theory.\n")
print(f"True or false, Mr. Python Interpreter, floatOne == decOne: {floatOne == decOne}\n") #BOOLEAN EXPRESSION REQUIREMENT 1/1, STRING FORMATTING REQUIREMENT 2/1
print("Well, that settles that.  Even internally, they are not the same.  ")

print("Clearly, if we need decimals to work the way we expect from school, the Decimal() version is what we need to use.\n")

##################
#String Data Type#
##################

print("Next, despite having already demonstrated basic competency using string formatting in combination with numeric data type manipulation, let's spend a moment on string variable manipulation.")
print("\nFirst, we'll define some string variables and display them one by one.")

prefixOne = "de"
prefixTwo = "un"
suffixOne = "able"
suffixTwo = "ed"
coreOne = "tract"
coreTwo = "tect"

print(f"\n{prefixOne=}\n{prefixTwo=}\n{suffixOne=}\n{suffixTwo=}\n{coreOne=}\n{coreTwo=}\n") #STRING FORMATTING REQUIREMENT

print("Now that we have defined and output the pieces, lets try some string concatenation.\n")

print("(Below:[prefixTwo+prefixOne+coreTwo+suffixTwo])\n")
print(f"When a ninja runs up on you quietly, they do so: {prefixTwo+prefixOne+coreTwo+suffixTwo}.\n") #STRING CONCATENATION

print("(Below:[prefixOne+coreTwo.replace('c','s')+suffixOne])\n")
print(f"When those ninjas age and take office jobs, but hate staying until 5pm, it's clear that they find their new work : {prefixOne+coreTwo.replace('c','s')+suffixOne}.\n") #USE OF STRING METHODS

print("(Below:[('-a-'.join([((coreTwo.replace('c',''))+'e')]*2))+'s'] and [prefixTwo+coreOne+suffixOne])\n")
print(f"Their employment records show that despite numerous {('-a-'.join([((coreTwo.replace('c',''))+'e')]*2))+'s'}, management found correcting the repeated behavior of early departure to be {prefixTwo+coreOne+suffixOne}.\n") #USE OF STRING METHODS, FORMATTING, AND CONCATENATION

print("(Below:[prefixOne+coreOne+suffixTwo])\n")
print(f"Ultimately, they let the behavior slide in order to avoid their workers shifting from feeling appreciated to {prefixOne+coreOne+suffixTwo}.\n")

iAmLeaving = True #BOOLEAN VARIABLE STORAGE REQUIREMENT 1/1

print(f"Now, that I have demonstrated competency in the use of several arithmetic data types and string manipulation, will I throw a smoke bomb and disappear? {iAmLeaving}\n")
print("      o               (_______)           ")
print("  o      o             (_____)            ")
print("o                       (___)             ")
print("            o            (_)              ")
print("              o...o.......o               \n")
