#TASK 1 BONUS
#Ice cream BO-GO

flavors = ['Vanilla', 'Butter Pecan', 'Chocolate', 'Pistachio', 'Rocky Road']

for flavor_1 in flavors:
    for flavor_2 in flavors:
        print(flavor_1, flavor_2)

# #TASK 2 BONUS

flavors = ['Vanilla', 'Butter Pecan', 'Chocolate', 'Pistachio', 'Rocky Road']

for flavor_1 in flavors:
    for flavor_2 in flavors:
        if flavor_1 == flavor_2:
            print('Double', flavor_1)
        else:
            print(flavor_1, flavor_2)

#TASK 3 BONUS
#Task 3: No Repeats!  

#FIRST attempt. This one is difficult. new_set slice has no effect. Might work better with a while loop.

# flavors = ['Vanilla', 'Butter Pecan', 'Chocolate', 'Pistachio', 'Rocky Road']

# for flavor_1 in flavors:
#     new_set = []
#     for flavor_2 in flavors:
#         print(flavor_1, flavor_2)
#         new_set = flavors[1:]

# #SECOND attempt

# flavors = ['Vanilla', 'Butter Pecan', 'Chocolate', 'Pistachio', 'Rocky Road']

# for flavor_1 in flavors:
#    new_set = []
#    print(flavor_1, flavor_2)
# new_set = flavors[1:]

#THIRD attempt. Prints only the first combo. I'm slicing incorrectly, or at least to no postive effect. Going back to for loop

# flavors = ['Vanilla', 'Butter Pecan', 'Chocolate', 'Pistachio', 'Rocky Road']

# while len(flavors) > 1:
#      for flavor_1 in flavors:
#         for flavor_2 in flavors:
#          print(flavor_1, flavor_2)
        
#          flavors = flavors[1:]

#FOURTH attempt. Could not figure it out.

# flavors = ['Vanilla', 'Butter Pecan', 'Chocolate', 'Pistachio', 'Rocky Road']

# for flavor_1 in flavors:
#     for flavor_2 in flavors[1:]:
#         print(flavors, flavor_2)

