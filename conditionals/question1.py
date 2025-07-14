# age categorization

user_age = int(input('Enter age: '))

if user_age < 13:
    print("child")
elif user_age < 19:
    print('teenager')
elif user_age < 59:
    print('Adult')
else:
    print('Senior')
