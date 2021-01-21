import re

class Traveler():
    def __init__(self,firstName,lastName,emailId,city,mobileNo):

        self.firstName = firstName
        self.lastName = lastName
        self.emailId = emailId
        self.city = city
        self.mobileNo = mobileNo

    def display(self):
        print("First Name: ", self.firstName)
        print("Last Name: ", self.lastName)
        print("Email-Id: ", self.emailId)
        print("City Name: ", self.city)
        print("Mobile No.: ", self.mobileNo)

def isValidMobileNo(n):
    m=re.fullmatch("[6-9][0-9]{9}",n)
    if m!= None:
        return 1
    else:
        return 0

def isValidEmailId(email):

    result = email.find("@")
    if ((result == -1) or email.startswith("@")):
        return 0
    else:
        return 1



fn = input("My First Name is: ")
ln = input("My Last Name is: ")
cn = input("My Current city is: ")

while True:

    mn = input("My Mobile Number is: ")
    # ei = input("My Email-Id is: ")

    res = isValidMobileNo(mn)
    if res == 1:
        while True:
            email = input("Enter Email id: ")
            res1 = isValidEmailId(email)

            if res1 == 1:
                t = Traveler(fn, ln,email,cn, mn)
                t.display()
                break
            else:
                print("Invalid Email-Id...Plz Enter Again...")
        break
    else:
        print("Invalid mobile number...Plz Enter Again..")







