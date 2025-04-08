from services.meta_ads import get_meta_ads_data
from services.shopify import get_shopify_data
from models.insights import generate_insights

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/insights")
def insights():
    meta = get_meta_ads_data()
    shopify = get_shopify_data()
    return jsonify(generate_insights(meta, shopify))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
