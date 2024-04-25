print('Welcome to the Fail Calculator')
print('This calculator will take your grade and tell you your percentage.')
points_total = float (input('How many points could you earn?'))
points_earned = float (input('How many points did you earn?'))
grade = ((points_earned)/(points_total))*(100)
print('Your grade was ', grade)
if grade > 89:
    print('You got an A, good job!')
elif grade > 79: 
    print('You got a B, nice!')
elif grade > 69: 
    print('You got a C, pretty average!')
elif grade > 59: 
    print('You got a D, good enough I suppose.')
else:
    print('You got an F, what a loser tbh.')