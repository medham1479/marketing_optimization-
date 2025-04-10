# shopify_data.py

import os
import pandas as pd
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta

try:
    import shopify
except ImportError:
    shopify = None

load_dotenv()

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
SHOPIFY_STORE = os.getenv("SHOPIFY_STORE_NAME")  
def get_shopify_data():
    """
    Returns real data if credentials are present, else returns mock.
    """
    if not SHOPIFY_API_KEY or not SHOPIFY_PASSWORD or not SHOPIFY_STORE or shopify is None:
        print("⚠️ Shopify credentials missing. Returning mock data.")
        return get_shopify_data()

    try:
        shop_url = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_PASSWORD}@{SHOPIFY_STORE}/admin"
        shopify.ShopifyResource.set_site(shop_url)

        orders = shopify.Order.find(status='any', limit=50)
        summary = {}

        for order in orders:
            for item in order.line_items:
                name = item.title
                revenue = float(item.price) * item.quantity
                summary[name] = summary.get(name, 0) + revenue

        return [{"product": k, "revenue": v, "sales": int(v // 100)} for k, v in summary.items()]

    except Exception as e:
        print(f"Shopify API error: {e}")
        return get_shopify_data()

def get_shopify_data():
    products = ["Boots", "Heels", "Loafers", "Sandals", "Sneakers"]
    today = datetime.today()

    shopify_summary = []

    for product in products:
        sales = random.randint(50, 300)
        revenue = round(sales * random.uniform(30.0, 100.0), 2)

        shopify_summary.append({
            "product": product,
            "sales": sales,
            "revenue": revenue
        })

    return shopify_summary