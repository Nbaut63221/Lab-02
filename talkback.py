# I want this programt to ask the user
# their name "what's your name?" and then
# I want the program to "HI, NAME"
# back where NAME is the user's actual name
# ask the user what year were they born?
# ask the user whats their favorite color?
#back where COLOR is the user's color
#back where YEAR is the user's year of birth


# step 1, ask the user what their name is
print(" what's your name?")
# step 2: input the user's name front the keyboard
# and save it into a variable so we can save it later
user_name = input()
# step 3: say hi back using the user's name
print(" Hi,"+ user_name + ".")


# step 2, ask the user what year were they born
print("what year were you born?")
year_born = input()
print("very nice old fart," + (year_born) + ".")

print("how old will you be in ten years?")
# input has to be current year not current age
current_year = input()

print( str(int(current_year) - int(year_born)+ 10))
# step 3, ask the user what their favorite color is

print("what's your favorite color?")
favorite_color = input ()
print("that's a great color. TURD!" + ".")


