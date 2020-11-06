n = int(input("Enter number of place within fibonacci series:"))
def fibonacci(n):
    a,b = 0,1
    if n <= 0:
        print("Invalid input")
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b
print(fibonacci(n))
