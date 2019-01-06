speed_limit = int(input('Enter the speed limit: '))
speed = int(input('Enter the recorded speed of the car: '))

if speed <= speed_limit:
    print('Congratulations, you are within the speed limit!')

else:
    if speed - speed_limit <= 20:
        fine = '100'
    elif speed - speed_limit <= 30:
        fine = '270'
    else:
        fine = '500'
    print('You are speeding and your fine is $' + fine + '.')

# 1 to 20 $100
# 21 to 30 $270
# 31 or above $500
