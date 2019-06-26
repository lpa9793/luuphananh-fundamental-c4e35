print('Answer the following algebra question:')
question={'If x=8, then what is the value of 4(x+3)?':[35,36,40,44]}

for key in question:
    print(key)
    for i in range(1,5):
        print(str(i)+'. ',question[key][i-1])
correct_answer=4
my_answer=int(input('\nYour choice: '))
if my_answer==correct_answer:
    print('Bingo')
else:
    print(':(')