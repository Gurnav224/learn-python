
user_age = int(input('Enter age: '))
day = input('Enter day eg: wednesday ')

price = 0

if user_age > 18 :
    price = 12
    print('movie ticket price ${price} for adult')
else:
    price = 8
    print('movie ticker price ${price} for children')

if(day == 'wednesday'):
    print('Price have discount', price - 2)
