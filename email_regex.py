import re

def isValidEmailId():
    s = input("Enter Your Email-Id: ")
    m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
    if m != None:
        print("Valid Mail Id");
    else:
        print("Invalid Mail id")

isValidEmailId()