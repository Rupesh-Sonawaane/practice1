import datetime


date1 = input("Enter the Checkin date: ")
d,m,y = date1.split("/")
d = int(d)
m = int (m)
y = int (y)

datecheckin =datetime.date(y,m,d)
print(datecheckin)

date2 = input("Enter the Checkout date: ")
d,m,y = date2.split("/")
d = int(d)
m = int (m)
y = int (y)

datecheckout =datetime.date(y,m,d)
r = print(datecheckout-datecheckin)
print(r)

