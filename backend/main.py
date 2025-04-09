from flask import Flask, jsonify, request
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
    try:
        campaign = request.args.get("campaign", "all")
        data = get_meta_ads_data()

        # Filter by campaign if applicable
        if campaign != "all":
            data = [d for d in data if d["campaign"] == campaign]

        forecast_data = generate_forecast(data)

        if not forecast_data:
            return jsonify({"error": "No data available to forecast."}), 400

        return jsonify(forecast_data)
    except Exception as e:
        print("❌ Forecast Error:", e)
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/abtest")
def abtest():
    meta_data = get_meta_ads_data()
    result = run_ab_test(meta_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
