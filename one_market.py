#!/usr/bin/python3
for i in range(1000):
    print(" ")
    print(" ")
    choose = input(
        "Choose from the categories below \n- Fruits\n- Phones\n- Vegetables\n- Drinks\n- Clothes\n- Art_object\n- Shoes\n- Cars (rentals)\nName of categories: ")

    if choose == "Fruits":

        print("                                           ")
        print("----------------FRUITS----------------")
        print("                                           ")
        # This is alist of fruits and thier prices
        fruit = {'orange': '100 Rwf -200 Rwf',
                 'Banana': '100 Rwf - 150 Rwf',
                 'mango': '200 Rwf - 300 Rwf',
                 'melons': '2500 Rwf - 3500 Rwf',
                 'apples': '400 Rwf - 500 Rwf',
                 'Papayas': '700 Rwf - 1000 Rwf',
                 'Pineapples': '300 Rwf - 500 Rwf',
                 'Lemons': '100 Rwf -300 Rwf'
                 }

        for keys, values in sorted(fruit.items()):
            print("{}: {}".format(keys, values))


    elif choose == "Phones":

        print("                                           ")
        print("----------------PHONES----------------")
        print("                                           ")
        # This is a list of phones from different companies and their prices
        phones = {
            'iphone 14 pro max (128GB 6GB RAM)': '1M Rwf',
            'iphone 14 pro (128GB 6GB RAM)': '1.2M Rwf',
            'iphone 14 plus (128GB 6GB RAM)': '783571 RWf',
            'iphone 13 pro max (128GB 6GB RAM)': '892551 Rwf',
            'iphone 13 pro (128GB 6GB RAM)': '972107 Rwf',
            'iphone 13 (128GB 6GB RAM)': '799918 Rwf',
            'iphone 13 mini (128GB 4GB RAM)': '730170 Rwf',
            'Samsung S23 Ultra (256GB 8GB RAM)': '1.1M Rwf',
            'Samsung Galaxy S23 (128GB 8GB RAM)': '811906 Rwf',
            'Samsung A53 5GB (128GB 4GB RAM)': '489323 Rwf',
            'Samsung Galaxy S10 (128GB 8GB RAM)': '391240 Rwf',
            'Samsung Galaxy A13 (32GB 3GB RAM)': '158022 Rwf',

        }

        for keys, values in sorted(phones.items()):
            print("{}: {}".format(keys, values))

    elif choose == "Vegetables":
        print("                                           ")
        print("----------------VEGETABLES----------------")
        print("                                           ")
        # Group of vegetables
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


    elif choose == "Drinks":

        print("                                           ")
        print("----------------DRINKS----------------")
        print("                                           ")
        # list of drinks and their prices
        drinks = {'Inyange mango juice': '800 Rwf -900 Rwf',
                  'Inyange apple juice': '800 Rwf - 900 Rwf',
                  'citron plastic soda': '800 Rwf - 1000 Rwf',
                  'vanilla yogurt 300ml': '700 Rwf - 800 Rwf',
                  'pineapple plastic soda ': '800 Rwf - 1000 Rwf',
                  'coca-cola free sugar plastic soda': '900 Rwf - 1000 Rwf',
                  'Embe juice small size': '400 Rwf -500 Rwf',
                  'Energy drink': '500Rwf -600Rwf'}

        for keys, values in sorted(drinks.items()):
            print("{}: {}".format(keys, values))


    elif choose == "Clothes":

        print("                                           ")
        print("----------------CLOTHES----------------")
        print("                                           ")
        # lists of clothes and their prices
        clothes = {'T-shirts': '2500 Rwf -5000 Rwf',
                   'Skirts': '3000 Rwf - 6000 Rwf',
                   'Trousers': '8000 Rwf - 12000 Rwf',
                   'Shorts': '3000 Rwf - 6000 Rwf',
                   'Jackets': '5000 Rwf - 10000 Rwf',
                   'Dresses': '6000 Rwf - 15000 Rwf',
                   'Socks': '500 Rwf - 1500 Rwf',
                   'Sweaters': '5000 Rwf - 8000 Rwf',
                   'Tights': '2500 Rwf - 4000 Rwf'
                   }
        for keys, values in sorted(clothes.items()):
            print("{}: {}".format(keys, values))

    elif choose == "Art_object":

        print("                                           ")
        print("----------------ART OBJECTS----------------")
        print("                                           ")
        Art_object = {'artistique painting': '8000 Rwf -15000 Rwf',
                      'pearl necklace': '5000 Rwf - 1000 Rwf',
                      'Imigongo': '20000 Rwf - 35000 Rwf',
                      'Floret hand woven Rwandan basket': '25000 Rwf - 30000 Rwf',
                      'colorful basket wall decor': '2500 Rwf - 40000 Rwf',
                      'Rwanda Beads ': '7000 Rwf - 1000 Rwf',
                      'small wooden sculpture in the shape of a tamtam and gorilla for key rings ': '500 Rwf - 1000 Rwf',
                      'Rwanda flag bracelt': '3000 Rwf -5000 Rwf'

                      }

        for keys, values in sorted(Art_object.items()):
            print("{}: {}".format(keys, values))

    elif choose == "Shoes":

        print("                                           ")
        print("----------------SHOES----------------")
        print("                                           ")
        # The list of shoes by category.....to be continued
        shoes = {'Sports shoes': '35000 Rwf - 50000 Rwf',
                 'Men’s Dress shoes': '30000 Rwf - 50000 Rwf',
                 'Women’s Dress shoes': '22000 Rwf - 45000 Rwf',
                 'Slippers': '8000 Rwf - 25000 Rwf',
                 'Sneakers': '20000 Rwf - 40000 Rwf',
                 'Ballerina': '8000 Rwf - 15000 Rwf',
                 'Sandals': '12000 Rwf - 15000 Rwf',
                 'Loafers': '15000 Rwf - 20000 Rwf',
                 'Boots': '30000 Rwf - 45000 Rwf'
                 }

        for keys, values in sorted(shoes.items()):
            print("{}: {}".format(keys, values))

    elif choose == "Cars":

        print("                                           ")
        print("----------------CARS----------------")
        print("                                           ")
        # The lists of cars and their prices
        Cars = {'hyundai tucson 2022': '$2535 - negotiable',
                'RAV4 2016 Toyota ': '$1740 to $2000',
                'Toyota Land Cruiser Prado': '$4700- negotiable',
                '2021 Mercedes-Benz GLB 250 SUV ': '$5805- negotiable',
                '4x4 jeep truck': '$5835- negotiable',
                'McLaren 720S': '$30500- negotiable',
                'BMW M3/M4': '$9095 - $10,000',
                'Mercedes Benz Maybach Eqs Suv': '$8,924 - negotiable',
                'Toyota Bus ': '$5,924 - negotiable'

                }

        for keys, values in sorted(Cars.items()):
            print("{}: {}".format(keys, values))

    else:
       print("                                           ")
       print("----------------{} is not available!----------------".format(choose))
       print("                                           ")
       print(
            "The available categories are \n- Fruits\n- Phones\n- Vegetables\n- Drinks\n- Clothes\n- Art_object\n- Shoes\n- Cars (rentals)")
       print("NB:The categories are  case sensitive")
    # Thank you All
