print('This is a pretty basic calculator.')
print('Call it Calculator.')
print('I dont really know what to tell you, its a calculator.')
first_num = input('Whats your first number?')
symbol = input('What would you like to do? -,+,*, or /')
second_num = input('Whats your second number?')
if symbol == ('-'):
    answer = int(first_num) - int(second_num) 
    print(answer)
elif symbol == ('+'):
    answer = int(first_num) + int(second_num)
    print(answer)
elif symbol == ('*'):
    answer = int(first_num) * int(second_num)
    print(answer)
elif symbol == ('/'):
    answer = int(first_num) / int(second_num)
    print(answer)
else:
    print('Thats not an option.')