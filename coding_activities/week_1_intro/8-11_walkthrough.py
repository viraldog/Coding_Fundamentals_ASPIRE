# this is a comment, the program ignores lines starting with a (#) 
# so we can use them to describe our code

# This line prints a message to the terminal when you run it
# print("Hello world!")

# We can save things as variables
# name = "Isabelle"       # this is called a string (remember to put the "" around all your text)
# age = 96                # this is called an integer (int)
# height_inches = 3000.5  # this is called a float (number with decimals)
# is_alive = True         # this is called a boolean (bool) (True or False only)

# You can print anything
# print(name)
# print(age)
# print(height_inches)
# print(is_alive)

# you can only do math to numbers
# a = 4
# b = 6
# print((a + b))
# print((a - b))
# print((a * b))

# You can't do math to strings
# c = "5"
# d = "3"
# print(c + d) # this wont work, itll print 53

# Just make sure to not misspell anything
# print(height) # this wont work, whe havent defined what height is

# you can ask the user for input, and save that
# name = input("What's your name? ")
# print(f"Hello {name}!") # this f tells the program to look for variables, and we put the variable inside the curly brackets {}

# This asks the user for their age and converts it to an integer
# age = int(input("How old are you? "))

# now that it is a number, we can do math to it
# double_age = age * 2
# print(double_age)

# We can use if/else statements to have our program make decisions
# if age < 18:    # if the user's age is less than 18, they are a kid
#     print("You're a kid!")
# else:           # otherwise, they are an adult
#     print("You're an adult!")



# -----------------------------------------------------------------------------------

# Let's actually make a program now

# Ask the user's name
name = input("What's your name? ")

# Ask for their age and convert the input to a number
age = int(input("How old are you? "))

# Calculate how many years until they are 18
years_until_18 = 18 - age

# Respond based on their age
if age < 18:
    print(f"Hi {name}, you'll be 18 in {years_until_18} years!")
else:
    print(f"Hi {name}, you're already an adult!")

# Ask the user's name
name = input("What's your name? ")

# Ask for their favorite food
food = input("What's your favorite food? ")

# Ask them to pick a number and convert to int
number = int(input("Pick a number between 1 and 10: "))

# Decide a personality trait based on even or odd number
if number % 2 == 0:
    mood = "adventurous"
else:
    mood = "mysterious"

# Final fortune output
print(f"\nHi {name}, based on your love for {food} and your number choice,")
print(f"we think you're a very {mood} person. Keep being awesome!")
