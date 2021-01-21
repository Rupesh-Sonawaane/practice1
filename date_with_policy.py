import datetime

def enter_date():
    dis_input = input("Type Date dd/mm/yyyy: ")
    d = datetime.datetime.strptime(dis_input,'%d/%m/%Y').date()
    return d


travel_date = enter_date()
cancelation_date = datetime.date.today()

r = (travel_date - cancelation_date)
if r.days > 15 :
    print("Sorry..You can not cancel the Bookings..")
else:
    print("Cancellation process started..wait for some time...")