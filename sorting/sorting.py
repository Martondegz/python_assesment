user=raw_input("enter words, comma separated> ")
user=user.split(",")
user=sorted(user)
print ",".join(user)