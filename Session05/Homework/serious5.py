def is_inside(a,b):
    # if len(a)!=2 or len(b)!=4:
    #     print('sai tham so')
    #     return
    if b[0]<a[0]<b[0]+b[2] and b[1]<a[1]<b[1]+b[3]: 
        return True
    else: 
        return False
#Test
test=is_inside([200,120],[140,60,100,200]) #width=100, height=200
if test == True:
   print("Your function is correct")
else:
   print("Ooops, bugs detected")