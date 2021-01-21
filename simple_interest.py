p=int(input("Enter Principle amount: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time period: "))
SI=p*r*t/100
print("The Interest on principle {} with rate of interest {} for time perid {} is {}".format(p,r,t,SI))
