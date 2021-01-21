import datetime

def obtaindate():
    date_input = input("Type Date dd/mm/yyyy: ")
    d = datetime.datetime.strptime(date_input, '%d/%m/%Y').date()
    return d

datecheckin = obtaindate()
datecheckout = obtaindate()
print(datecheckout-datecheckin)