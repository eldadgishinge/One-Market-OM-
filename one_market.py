#!/usr/bin/python3

#This is alist of fruits and thier prices
fruit= {'orange' : '100 Rwf -200 Rwf',
        'Banana' : '100 Rwf - 150 Rwf',
        'mango'  : '200 Rwf - 300 Rwf',
        'melons' : '2500 Rwf - 3500 Rwf',
        'apples' : '400 Rwf - 500 Rwf',
        'Papayas': '700 Rwf - 1000 Rwf',
        'Pineapples':'300 Rwf - 500 Rwf',
        'Lemons' : '100 Rwf -300 Rwf'

for keys, values in sorted(fruit.items()):
    print("{}: {}".format(keys, values))
