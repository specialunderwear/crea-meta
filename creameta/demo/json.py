from creameta.meta import JSONMetaNonsence

# create password class that hold passwords
class passwords(object):
    __metaclass__ = JSONMetaNonsence

    henk = 'uy98jjd'
    piet = 'y98adkkjhd77'
    kees = 'god'
    marietje = 'password1'
    write = True

# prove that it is stored encrypted
print passwords

# create an instance
a = passwords()

# prove that all passwords are properly hashed
print a

try:
    # prove that attackers can not read the information out of the passwords
    # object
    print a.henk
    print a.piet
    print a.kees
    print a.marietje
except Exception as e:
    print e

raw_input("Press Enter to continue...")

# create a password class to read the pawwords
class passwords(object):
    __metaclass__ = JSONMetaNonsence

    def __str__(self):
        return "passwords storage opened"

# show that this class is of the original type used to store the passwords
print passwords

# create an instance to read the passwords
b = passwords()

print b
print dir(b)

print b.henk
print b.piet
print b.kees
print b.marietje
