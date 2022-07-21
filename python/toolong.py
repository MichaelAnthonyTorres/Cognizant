def too_long(n):
    length = len(n)
    if length > 140:
        return True
    else:
        return False

print(too_long("This is a test"))
print(too_long("This is going to be an axtremely long quote to make sure that the code is running correctly. Although 140 characters doesnt seem like a lot of characters it can be sometimes. Im not even sure if this is 140 yet."))
