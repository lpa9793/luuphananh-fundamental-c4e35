size=[5,7,300,90,24,50,75]
print("Hello, my name is Audrey and these are my sheep sizes")
print(size)
print("Now my biggest sheep has size",max(size),"let shear it")
pos=size.index(max(size))
size[pos]=8
print("After shearing, here is my flock")
print(size)
print()

j=0
while j<3:
    j += 1
    print('MONTH',j,':')
    for i in range(len(size)):
        size[i]=size[i]+50
    print("One month has passed, now here is my flock")
    print(size)
    if j==3:
        break
    print("Now my biggest sheep has size",max(size),"let shear it")
    pos=size.index(max(size))
    size[pos]=8
    print("After shearing, here is my flock")
    print(size)
    print()

total_size=sum(size)
print("My flock has size in total:",total_size)
money=total_size*2
print("I would get",total_size,"* 2$","=",money,"$")