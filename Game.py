import random

rand = random.randrange(1,20)
#print('rand' ,rand)
for i in range(3):
    userInput = int(input('Enter number: '))
    if userInput == rand:
        print('Hey you guess right number' ,rand)
        break
    elif userInput > rand:
        print('So large')

    elif userInput < rand:
        print('So small')
else:
    print('You are excided number of trials')

