import random

household_items = ['toothbrush', 'towel', 'dish soap', 'lamp', 'pillow', 'coffee mug', 'scissors', 'remote control']

print('In this game you will have to guess a certain household item from the list below...')
print()

for items in range(len(household_items)): #makes the list readable
    print(household_items[items])

comp_choice = random.choice(household_items)
print()
while True:
    user_choice = input('Which item on the list is it?? ')

    if user_choice == comp_choice:
        print('You guessed it!!')
        break
    else:
        print('guess AGAIN!')

    