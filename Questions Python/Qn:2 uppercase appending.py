#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
#Use list and append




user = raw_input("write an input..")# writes a prompt for the user
list = [] #creates a empty list
list.append(user)#adding the users input on the list
for item in list: #for every item added on the list we print the uppercase
    print  item.upper()