"""
Name:Duncan Staats
Date:12/16/2024
Lesson: Tuples
"""

# Tuples are a heterogeneous (mixed types), immutable data structure
# How to pronounce, from the Python creator:
"""
I pronounce tuple too-pull on Mon/Wed/Fri and tub-pull on Tue/Thu/Sat. 
On Sunday I don't talk about them. :) 
"""
# The look like an ordered pair in math

# Make tuple with two items
my_tuple = ("3",4)
print(my_tuple)
# Make tuple with one item
lonely_tuple = (5,) #not a tuple without a comma and the ( )
print(lonely_tuple)

# You access elements from them using [ ] just like strings
print(my_tuple[0])

# Also like strings, you can only concatenate tuples with other tuples
not_lonely_tuple = my_tuple + (5,)
print(not_lonely_tuple)
integer_tuple = (int(my_tuple[0]),4,5)
print(integer_tuple)
# I heard you like tuples...
# so you can also put tuples inside your tuples
# need two [] to access them.
character_info = (("Rosalie",100),("Cedric",75),("Shana",94))
print(character_info[1][0])

########## Exercise ##########

"""
In the file linear_calculations.py, complete the slope and distance
function. Each function takes in two tuples, representing two (x,y) points,
and returns the slope or distance as a float. 
"""