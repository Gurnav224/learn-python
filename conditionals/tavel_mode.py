
distance = int(input('enter distance: '))

mode = ''

if distance < 3:
    mode = 'Walk'
elif distance < 15:
    mode = 'Bike'
else:
    mode = 'Car'

print('Mode of Travel', mode)