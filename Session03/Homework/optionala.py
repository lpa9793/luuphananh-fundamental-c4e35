import random
word="hexagon"
correct = word
jumble=""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print(jumble)
guess=input("Your guess: ")
if guess == correct:
    print("Hura")
else:
    print(":(")
