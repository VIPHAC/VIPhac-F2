import os 
os.system ('clear')

print('\n \tp جمع')
print('\n \tc طرح')
print('\n \ty قسمة')
print('\n \tx ضرب')

calculations = input('\n\nwhats kind of calculation ')
os.system ("clear")
if calculations.lower() == 'p':
    a = input ('\nwrite a number: ')
    b = input ('another number: ')
    a = int(a)
    b = int(b)
    p = a + b
    print(int(p))
elif calculations.lower() == 'c':    
    a = input ('\nwrite a number: ')
    b = input ('another number: ')
    a = int(a)
    b = int(b)
    c = a - b
    print(int(c))
elif calculations.lower() == 'x':
    a = input ('\nwrite a number: ')
    b = input ('another number: ')
    a = int(a)
    b = int(b)
    x = a * b
    print(int(x))
elif calculations.lower() == 'y':
    a = input ('\nwrite a number: ')
    b = input ('another number: ')
    a = int(a)
    b = int(b)
    y = a / b
    print(int(y))
else:
    os.system('clear')
    print('Not Found')
