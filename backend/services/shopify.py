import random

def get_shopify_data():
    products = ['Sneakers', 'Boots', 'Sandals', 'Heels', 'Loafers']
    data = []

    for _ in range(5):
        product = random.choice(products)
        units = random.randint(50, 300)
        unit_price = random.uniform(30, 120)
        revenue = round(units * unit_price, 2)

        data.append({
            'product': product,
            'sales': units,
            'revenue': revenue
        })

    return data
