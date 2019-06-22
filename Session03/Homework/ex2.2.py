#mua nha 1.2 ty
i=0
while True:
    i += 1
    m=21*(1+0.065)**i
    if m>=1200:
        print("So nam can gui tien la:",i)
        break

#mua nha 1.2 ty (gia nha tang 1%/nam)
i=0
while True:
    i += 1
    m=21*(1+0.065)**i
    if m>=(1200*(1+0.01)**i):
        print("So nam can gui tien la:",i)
        break