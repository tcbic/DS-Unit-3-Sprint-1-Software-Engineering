import random
from random import randint, sample, uniform
from acme import Product

#Useful to use with random.sample to generate names.
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Randomly generates a given number of products and returns them
    as a list."""
    products = []
    for _ in range(num_products):
        name = " ".join(random.sample(ADJECTIVES, 1) + random.sample(NOUNS, 1))
        prod = Product(name)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(prod)
    return products

def inventory_report(products):
    """Takes a list of products and prints a summary."""
    unique_names = []
    total_price = 0
    total_weight = 0
    total_flammability = 0
    number_of_products = len(products)
    
    for product in products:
        if product.name not in unique_names:
            unique_names.append(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    print("ACME CORPORATION OFFICIAL INVENTORY")
    print(f"Unique product names: {len(unique_names)}" )
    print(f"Average price: {total_price/number_of_products}")
    print(f"Average weight: {total_weight/number_of_products}")
    print(f"Average flammability: {total_flammability/number_of_products}")

if __name__ == '__main__':
    inventory_report(generate_products())
