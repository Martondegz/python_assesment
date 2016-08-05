#user input
user=raw_input("Type your words")

#splits words after every comma
user=user.split(",")

#Sorts the user input in alphabetical order
user=sorted(user)

#Joins the sorted strings with a comma after every word
print ",".join(user)
