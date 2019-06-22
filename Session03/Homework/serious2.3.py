size=[5,7,300,90,24,50,75]
print("Hello, my name is Audrey and these are my sheep sizes")
print(size)
print("Now my biggest sheep has size",max(size),"let's shear it")
pos=size.index(max(size))
size[pos]=8
print("After shearing, here is my flock")
print(size)
