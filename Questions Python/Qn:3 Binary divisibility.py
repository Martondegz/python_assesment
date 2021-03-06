"""Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Use list and .join"""
#Ask for user input
user = raw_input("Input Digits separated by a comma...")

#Defining Binary Check Function
def binary_check(number):
    for char in number:    #For every interger in the number
        if int(char) >= 0 and int(char) <=1:
            return True
        else:
            return False

#Split the user-input after every comma
user_list  = user.split(",")
#Temporary Variable for holding the output
new_list = []
#For every numeber in user_list
for item in user_list:
    if binary_check(item) and int(item) % 5 == 0 and len(item)==4:
        new_list.append(item)      #Add the item if true to new_list

print new_list  #print new_list
