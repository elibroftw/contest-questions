time = input()
hour, minute = int(time[0:2]), time[3:5]
if hour == 6:
    if minute == '00': print('09:00')
    elif minute == '20': print('09:40')
    elif minute == '40': print('10:10')
elif hour == 14:
    if minute == '00': print('17:00')
    elif minute == '20': print('17:40')
    elif minute == '40': print('18:20')
elif hour == 5:
    if minute == '00': print('07:00')
    elif minute == '20': print('07:40')
    elif minute == '40': print('08:20')
elif hour == 13:
    if minute == '00': print('15:00')
    elif minute == '20': print('15:40')
    elif minute == '40': print('18:20')
elif hour == 8 or hour == 17:
    if minute == '00': print(hour + 3, ':', minute, sep='')
    elif minute == '20': print(hour + 3, ':', 10, sep='')
    elif minute == '40': print(hour + 3, ':', 20, sep='')
elif hour == 9 or hour == 18:
    if minute == '40': print(hour + 2, ':', 50, sep='')
    elif minute == '00': print(hour + 2, ':', 30, sep='')
    elif minute == '20': print(hour + 2, ':', 40, sep='')
elif hour == 7 or hour == 16:
    if minute == '00': print(hour + 3, ':', 30, sep='')
    elif minute == '20': print(hour + 3, ':', 40, sep='')
    elif minute == '40': print(hour + 3, ':', 50, sep='')
elif hour == 15:
    if minute == '00': print('19:00')
    elif minute == '20': print('19:10')
    elif minute == '40': print('19:20')
else:
    hour = hour + 2
    if hour < 10: hour = '0' + str(hour)
    elif hour != str(hour) and hour > 23: hour = '0' + str(hour - 24)
    print(hour, ':', minute, sep='')
