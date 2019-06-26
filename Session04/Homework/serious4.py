print('Answer the following questions:')
question_1={'If x=8, then what is the value of 4(x+3)?':[35,36,40,44,4]}
question_2={'Jack scored these marks in 5 math tests: 49, 81, 72, 66, and 52. What is the mean?':['About 55','About 65','About 75','About 85',2]}
correct=0
for key in question_1:
    print(key)
    for i in range(1,5):
        print(str(i)+'. ',question_1[key][i-1])
my_answer_1=int(input('\nYour choice: '))
correct_answer_1=question_1[key][4]
if my_answer_1==correct_answer_1:
    print('Bingo')
    correct+=1
else:
    print(':(')

for key in question_2:
    print(key)
    for i in range(1,5):
        print(str(i)+'. ',question_2[key][i-1])
my_answer_2=int(input('\nYour choice: '))
correct_answer_2=question_2[key][4]
if my_answer_2==correct_answer_2:
    print('Bingo')
    correct+=1
else:
    print(':(')
print()
print('You correctly answer',correct,'out of 2 questions')