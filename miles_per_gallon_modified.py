#!/usr/bin/env python3

print('The Miles Per Gallon Program \n')

milesDriven = float(input('Enter Miles Driven: \t\t'))
gallonsUsed = float(input('Enter Gallons of Gas Used: \t'))
costPerGallon = float(input('Enter Cost Per Gallon: \t\t'))

mpg = milesDriven / gallonsUsed
gasCost = gallonsUsed * costPerGallon
costPerMile = gasCost / milesDriven 

if (mpg % 1 != 0):
    print(f'\nMiles per Gallon: \t\t{round(mpg, 2)}')
else:
    print(f'\nMiles per Gallon: \t\t{round(mpg)}')

if (gasCost % 1 != 0):
    print(f'Total Gas Cost: \t\t${round(gasCost, 2)}')
else:
    print(f'Total Gas Cost: \t\t${round(gasCost)}')

print(f'Cost Per Mile: \t\t\t${round(costPerMile, 3)}')
print('\nBye!')

