import datetime

def acceptdate():
    dis_input = input("Type Date dd/mm/yyyy: ")
    d = datetime.datetime.strptime(dis_input,'%d/%m/%Y').date()
    return d


joining_date = acceptdate()
relieving_date = acceptdate()

result = (relieving_date-joining_date)
print(result)

if (result.days>365):
    r = result.days/365
    days=result.days%365
    print("experience duration ",int(r)," years", days," days")

