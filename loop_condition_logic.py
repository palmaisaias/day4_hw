#TASK 1
#Loop Condition Exploration

while True:
    best_player = input('Whos the best soccer player of all time? ')

    if best_player == 'Messi':
        print('That is the correct answer!')
        break
    else:
        print('Wrong. The answer is NOT that difficult...')

#TASK 2
#Conditional Exit

countdown = [5, 4, 3, 2, 1]
index = 0

print('Launch starting in...')

while index < len(countdown):
    print(countdown[index])
    index += 1

print('TAKEOFF!')