import mysql.connector
class Traveller:

    id = ""
    fName = ""
    lName = ""
    city = ""
    mobNo = ""

    def check(self):

        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database = "traveller_info"
            )
            cursor=con.cursor()
            cursor.execute("INSERT INTO Traveller (id, fName, lName, city, mobNo) VALUES (?, ?, ?, ?, ?)", (Traveller.id,Traveller.fName, Traveller.lName, Traveller.city, Traveller.mobNo))
            # cursor.execute("select curdate();")
            # s=cursor.fetchone()
            # print(s[0])
            con.commit()
            print("Data added successfully")

        except Exception as e:
            if con:
                con.rollback()
                print("There is some problem",e)

        finally:
            if cursor:
                cursor.close()

            if con:
                con.close()

    def inputFromUser(self):
        Traveller.id = int(input("Enter your Id: "))
        Traveller.fName = input("Enter First Name: ")
        Traveller.lName = input("Enter Last Name: ")
        Traveller.city = input("Enter City Name: ")
        Traveller.mobNo = int(input("Enter Mobile No.: "))

    def display(self):
        print("My Id is: ",Traveller.id)
        print("First Name is: ",Traveller.fName)
        print("Last Name is: ", Traveller.lName)
        print("City Name is: ", Traveller.city)
        print("My Mobile Number is: ", Traveller.mobNo)


t = Traveller()
t.inputFromUser()
t.check()
t.display()


