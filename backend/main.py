from flask import Flask, jsonify
from flask_cors import CORS
from services.meta_ads import get_meta_ads_data
from services.shopify import get_shopify_data
from models.insights import generate_insights
from models.forecast import generate_forecast
from models.ab_test import run_ab_test

app = Flask(__name__)
CORS(app)

@app.route("/api/insights")
def insights():
    meta_data = get_meta_ads_data()
    shopify_data = get_shopify_data()
    result = generate_insights(meta_data, shopify_data)
    return jsonify(result)

@app.route("/api/forecast")
def forecast():
    meta_data = get_meta_ads_data()
    result = generate_forecast(meta_data)
    return jsonify(result)

@app.route("/api/abtest")
def abtest():
    meta_data = get_meta_ads_data()
    result = run_ab_test(meta_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
