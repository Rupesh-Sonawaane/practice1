def validateEmail():
    email = input("Enter Email id: ")
    result = email.find("@")
    if ((result == -1) or email.startswith("@")):
        print("InValid EmailId")
    else:
        print("Valid EmailId")

validateEmail()






