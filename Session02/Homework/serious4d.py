n=int(input("Enter a number: "))
for i in range(1,n+1):
    if i%2==1:
        print("x ", end="")
    else:
        print("* ", end="")