"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Use a sorting method"""
#user input
user=raw_input("Type your words")

#splits words after every comma
user=user.split(",")

#Sorts the user input in alphabetical order
user=sorted(user)

#Joins the sorted strings with a comma after every word
print ",".join(user)
