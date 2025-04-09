import os
import pandas as pd
import openai




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

    recommendations = generate_llm_recommendations(summary)

    return {
        "roi": df["roi"].mean(),
        "meta_summary": df.to_dict(orient="records"),
        "shopify_summary": shopify_data,
        "budget_suggestions": [], # Placeholder for budget suggestions
        "recommendations": recommendations
    }


def generate_llm_recommendations(summary_df):
    """
    Generate natural language marketing recommendations from A/B performance summary using LLM.
    """

    prompt = f"""
You are an expert marketing analyst helping a growth team optimize Meta Ads performance. Below is a summary of key metrics from an A/B test for two ad variants:

{summary_df.to_json(orient="records", indent=2)}

Your job is to analyze and interpret this data, and write 3 to 5 concise, high-impact recommendations to improve marketing performance.

Each recommendation should follow these guidelines:
- Address key metrics (CTR, CPC, conversion rate, ROI)
- Make clear comparisons between Variant A and Variant B
- Suggest **specific actions**: e.g., "increase budget for...", "test new creatives...", "pause variant B if..."
- Use short bullet points (1–2 sentences each)
- Avoid generic or vague suggestions

Respond only with the bullet points.
"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        response = openai.ChatCompletion.create(
         model= "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
)
        raw = response['choices'][0]['message']['content']
        lines = [line.strip("-• ") for line in raw.strip().split("\n") if line.strip()]
        return lines[:5] if lines else ["⚠️ No insights generated."]
    except Exception as e:
        return [f"LLM error: {e}"]