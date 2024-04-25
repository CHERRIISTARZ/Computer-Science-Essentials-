print('Welcome to the Fail Calculator')
print('This calculator will take your grade and tell you your percentage.')
points_total = float (input('How many points could you earn?'))
points_earned = float (input('How many points did you earn?'))
grade = ((points_earned)/(points_total))*(100)
print('Your grade was ', grade)
if grade > 59:
    print('You passed, good job!')
elif grade < 59: 
    print('How do you fail that bad bro?')
else:
    print('You broke the game.')