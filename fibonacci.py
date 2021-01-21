class Fibo_series():
    # def __init__(self,n):
    #     self.n=n

    def fiboseries(self,n):
        a=0
        b=1
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)

            for i in range(2,n):
                c = a + b
                a = b
                b = c
                print(c)

    def inputfromuser(self):
        numberofdigit = int(input("Enter no of digit "))
        return numberofdigit


f = Fibo_series()
# n1=f.inputfromuser()
f.fiboseries(f.inputfromuser())