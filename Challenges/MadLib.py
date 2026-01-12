# In this assignment you will introduce yourself through a Mad Lib! 
# The program you create will ask for input that you will store in variables that you will then concatenate in a Mad Lib. 
# You can use the following Mad Lib or come up something that may be more funny on your own. 
# You will submit the .py file along with a screenshot of the output of the program.

# Hello, my name is ____________________________. One thing I would like
# for you to know about me is when I am not programming I love to ______________________________________________.
# I also want you to know that I am a ____________________student who loves ________________________ but
# absolutely hates __________________________! The best way to describe my personality is __________________ and __________________.
# My personal philosophy or a strong belief that I have that guides me through my life is ____________________________.
# I am __________________________ to learn about programming!

# Printing a welcome message
print("----------------------")
print("Welcome to my Mad Lib!")
print("----------------------")

# Getting user inputs/name/hobby/student type/favorite subject/hated subject
# personality traits/Philosophy/learning motivation
name = input("What is your name?: ")
hobby = input("What do you love to do when you are not programming?: ")
student_type = input("What type of student are you?: ")
favorite_subject = input("What is your favorite subject?: ")
hated_subject = input("What subject do you absolutely hate?: ")
personality_traits = input("What are two words that describe your personality?: ")
philosophy = input("What is your personal philosophy or strong belief?: ")
learning_motivation = input("How do you feel about learning programming?: ")

# Creating the Mad Lib
mad_lib = "Hello, my name is " + name + ". One thing I would like for you to know about me is when \nI am not programming I love to " + hobby + ".\nI also want you to know that I am a " + student_type + " student who loves " + favorite_subject + "\nbut absolutely hates " + hated_subject + "! The best way to describe my personality is " + personality_traits + ".\nMy personal philosophy or a strong belief that I have that\nguides me through my life is " + philosophy + ".\nI am " + learning_motivation + " to learn about programming!"

# Print the Mad Lib
print("------------------------------------------------------------------")
print(mad_lib)
print("------------------------------------------------------------------")