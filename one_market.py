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
        }

for keys, values in sorted(fruit.items()):
    print("{}: {}".format(keys, values))

#Group of vegetables 
vegetables = {'Pumpkin': '300 Rwf - 400 Rwf',
         'Tomato': '150 Rwf - 180 Rwf',
         'Eggplant': '250 Rwf - 400 Rwf',
         'Green peas': '1500 Rwf - 2000 Rwf',
         'Corn': '400 Rwf - 500 Rwf',
         'Garlic': '100 Rwf - 200 Rwf',
         'Cucumber': '200 Rwf - 300 Rwf',
         'Onions': '100 Rwf -200 Rwf'
        }
for keys, values in sorted(vegetables.items()):
    print("{}: {}".format(keys, values))

#list of drinks and their prices
drinks= {'Inyange mango juice' : '800 Rwf -900 Rwf',
        'Inyange apple juice' : '800 Rwf - 900 Rwf',
        'citron plastic soda'  : '800 Rwf - 1000 Rwf',
        'vanilla yogurt 300ml' : '700 Rwf - 800 Rwf',
        'pineapple plastic soda ' : '800 Rwf - 1000 Rwf',
        'coca-cola free sugar plastic soda': '900 Rwf - 1000 Rwf',
        'Embe juice small size' : '400 Rwf -500 Rwf',
	'Energy drink' : '500Rwf -600Rwf' }

for keys, values in sorted(drinks.items()):
    print("{}: {}".format(keys, values))

#lists of clothes and their prices
clothes= {'T-shirts' : '2500 Rwf -5000 Rwf',
        'Skirts' : '3000 Rwf - 6000 Rwf',
        'Trousers'  : '8000 Rwf - 12000 Rwf',
        'Shorts' : '3000 Rwf - 6000 Rwf',
        'Jackets' : '5000 Rwf - 10000 Rwf',
        'Dresses': '6000 Rwf - 15000 Rwf',
        'Socks':'500 Rwf - 1500 Rwf',
        'Sweaters' : '5000 Rwf - 8000 Rwf',
        'Tights' : '2500 Rwf - 4000 Rwf'}

for keys, values in sorted(clothes.items()):
    print("{}: {}".format(keys, values))
