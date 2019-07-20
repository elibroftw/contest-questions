print('How many antennas?')
antennas = int(input())
print('How many eyes?')
eyes = int(input())

if antennas >= 3 and eyes <= 4:
    print('TroyMartian')
if antennas <= 6 and eyes > 2:
    print('VladSaturnian')
if antennas <= 2 and eyes <= 3:
    print('GraemeMercurian')
