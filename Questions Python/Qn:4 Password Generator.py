
"""Password Generator"""

#Code Packages random & string
import random
import string
#string.printable is all cahracters and symbols
#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
s =string.printable

#passlen is the number of character passwords the user wants
passlen = int(raw_input("How many Characters would you like...?\n"))

#joining the random password
p =  "".join(random.sample(s,passlen ))

#Print the random password
print p