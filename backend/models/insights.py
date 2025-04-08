import pandas as pd

def generate_insights(meta_data, shopify_data):
    df = pd.DataFrame(meta_data)

    df["ctr"] = df["clicks"] / df["impressions"]
    df["cpc"] = df["spend"] / df["clicks"]
    df["conversion_rate"] = df["conversions"] / df["clicks"]
    df["roi"] = (df["conversions"] * 30 - df["spend"]) / df["spend"]  

    summary = df.groupby("variant").agg({
        "ctr": "mean",
        "cpc": "mean",
        "conversion_rate": "mean",
        "roi": "mean"
    }).reset_index()

    recommendations = generate_recommendations(summary)

    return {
        "roi": df["roi"].mean(),
        "meta_summary": df.to_dict(orient="records"),
        "shopify_summary": shopify_data,
        "budget_suggestions": [], # Placeholder for budget suggestions
        "recommendations": recommendations
    }


def generate_recommendations(summary_df):
    recs = []

    try:
        variant_a = summary_df[summary_df["variant"] == "A"].iloc[0]
        variant_b = summary_df[summary_df["variant"] == "B"].iloc[0]
    except IndexError:
        return ["Insufficient data to compare A/B variants."]

    if variant_a["ctr"] > variant_b["ctr"] * 1.1:
        recs.append("📈 Variant A has a significantly higher CTR. Prioritize Video Ads.")
    elif variant_b["ctr"] > variant_a["ctr"] * 1.1:
        recs.append("📈 Variant B is attracting more clicks. Test Carousel formats more.")

    if variant_a["roi"] > variant_b["roi"] * 1.2:
        recs.append("💰 Variant A has much better ROI. Allocate more spend to Campaign A.")
    elif variant_b["roi"] > variant_a["roi"] * 1.2:
        recs.append("💰 Variant B has better ROI. Shift budget to Campaign B.")

    if variant_a["cpc"] < variant_b["cpc"]:
        recs.append("🧾 CPC is lower for Variant A — it's more efficient at driving clicks.")
    elif variant_b["cpc"] < variant_a["cpc"]:
        recs.append("🧾 CPC is lower for Variant B — optimize creatives for better cost control.")

    if variant_a["conversion_rate"] > variant_b["conversion_rate"] * 1.1:
        recs.append("⚡ Variant A converts better — target similar audiences.")
    elif variant_b["conversion_rate"] > variant_a["conversion_rate"] * 1.1:
        recs.append("⚡ Variant B is converting better — optimize landing pages accordingly.")

    if not recs:
        recs.append("🔄 Performance is similar between A and B. Continue monitoring.")

    return recs

