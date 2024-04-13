#FIRST attempt. Got it to work, but I have to tweek the output to the correct format
# import random

# food_item = ['oatmeal', 'cereal', 'apples', 'fried chicken', 'pizza', 'pupusas', 'tacos', 'coffee', 'orange slices', 'ribeye steak', 'yogurt', 'turkey sandwich', 'pb and j', 'rice and beans', 'rotisserie chicken', 'in n out', 'eggs and toast', 'salmon']
# week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# meals = ['Breakfast', 'Lunch', 'Dinner']



# for each_day in week:
#     print('Day of the week:', each_day)
#     #within this loop, we 'nest' another for loop to make use of another list
#     for meal in range(len(meals)):
#         random_food = random.choice(food_item) #originally put this right under the lists and it returned the same choice every time. Duh.
#         print('Having', random_food, 'for', meals[meal])  

#SECOND attempt. Cleaned up the output. Reduced 'print' to a single occurance
import random

food_item = ['oatmeal', 'cereal', 'apples', 'fried chicken', 'pizza', 'pupusas', 'tacos', 'coffee', 'orange slices', 'ribeye steak', 'yogurt', 'turkey sandwich', 'pb and j', 'rice and beans', 'rotisserie chicken', 'in n out', 'eggs and toast', 'salmon']
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
meals = ['breakfast', 'lunch', 'dinner']

for each_day in week:
    #within this loop, we 'nest' another for loop to make use of another list
    for meal in range(len(meals)):
        random_food = random.choice(food_item) #originally put this right under the lists and it returned the same choice every time. Duh.
        print(each_day, 'for', meals[meal], 'Im having', random_food)  