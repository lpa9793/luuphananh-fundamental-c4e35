i=int(input("Nhap so nam: "))
m=21*(1+0.065)**i
print("Sau",i,"nam co so tien la:",m,"trieu dong")

# Mua nhà 1.2 tỷ cần gửi ngân hàng bao nhiêu năm?
i=0
while True:
    i += 1
    m=21*(1+0.065)**i
    if m>=1200:
        print('so nam la',i)
        break