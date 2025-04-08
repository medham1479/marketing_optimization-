import pandas as pd

def generate_insights(meta_data, shopify_data):
    meta_df = pd.DataFrame(meta_data)
    shopify_df = pd.DataFrame(shopify_data)

    # Calculate basic KPIs
    total_spend = meta_df["spend"].sum()
    total_revenue = shopify_df["revenue"].sum()
    roi = total_revenue / total_spend if total_spend else 0

    # Predictive budgeting suggestions (mock logic)
    budget_suggestions = []
    for spend in [100, 300, 500, 800, 1000]:
        predicted_conversions = int(spend * roi * 0.1)
        predicted_roi = (predicted_conversions * 10 - spend) / spend * 100
        budget_suggestions.append({
            "spend": spend,
            "predicted_conversions": predicted_conversions,
            "predicted_roi": round(predicted_roi, 2)
        })

    # Group Shopify summary by product
    shopify_summary = (
        shopify_df.groupby("product")
        .agg({"revenue": "sum", "sales": "sum"})
        .reset_index()
        .to_dict(orient="records")
    )

    # Group Meta summary by campaign
    meta_summary = (
        meta_df[["campaign", "date", "impressions", "clicks", "conversions", "spend", "variant"]]
        .to_dict(orient="records")
    )

    # Automated recommendations
    recommendations = []
    avg_ctr = (meta_df["clicks"] / meta_df["impressions"]).mean()
    if avg_ctr < 0.05:
        recommendations.append("⚠️ CTR is low. Consider refreshing your creative.")
    else:
        recommendations.append("✅ CTR is healthy. Keep testing high-performing variants.")

    # Generate A/B test trends over time
    ab_trend_df = (
        meta_df.groupby(["date", "variant"])
        .agg({"clicks": "sum", "impressions": "sum"})
        .reset_index()
    )
    ab_trend_df["ctr"] = ab_trend_df["clicks"] / ab_trend_df["impressions"]

    # Pivot to get A and B in same row
    ab_trend_pivot = ab_trend_df.pivot(index="date", columns="variant", values="ctr").reset_index()
    ab_trend_pivot.columns.name = None
    ab_trend_pivot = ab_trend_pivot.rename(columns={"A": "ctr_A", "B": "ctr_B"})

    ab_trends = ab_trend_pivot.fillna(0).to_dict(orient="records")

    return {
        "roi": round(roi, 2),
        "budget_suggestions": budget_suggestions,
        "shopify_summary": shopify_summary,
        "meta_summary": meta_summary,
        "recommendations": recommendations,
        "ab_trends": ab_trends
    }
