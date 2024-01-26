def order_pizza(size, *toppings, **details):
    print(f'Ordered a {size} sizwd pizza with the following toppings:')
    for top in toppings:
        print(f'- {top}')
    print('\nDetails of the order-')
    for key, value in details.items():
        print(f'-{key}: {value}')

order_pizza('medium', 'pepperoni', 'olives', delivery=True, tip=5)