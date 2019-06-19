# calculating the factorial of n
n=int(input("Enter a number: "))
S=1
if n==0:
    print(n,end="")
    print("! = ",S)
else:
    for i in range(1,n+1):
        S=S*i
    print(n,end="")
    print("! = ",S)
