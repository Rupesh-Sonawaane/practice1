def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
f = int(input("Enter the number: "))
res = fact(f)
print(res)
