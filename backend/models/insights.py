import pandas as pd
from sklearn.linear_model import LinearRegression

def generate_insights(meta_data, shopify_data):
    total_spend = sum(d['spend'] for d in meta_data)
    total_revenue = sum(d['revenue'] for d in shopify_data)
    roi = total_revenue / total_spend if total_spend else 0

    df = pd.DataFrame(meta_data)
    df['ctr'] = df['clicks'] / df['impressions']
    df['cvr'] = df['conversions'] / df['clicks']
    df.fillna(0, inplace=True)

    model = LinearRegression()
    model.fit(df[['spend', 'ctr', 'cvr']], df['conversions'])

    # Predict for different spend scenarios
    test_spend = [100, 300, 500, 800, 1000]
    test_df = pd.DataFrame({
        'spend': test_spend,
        'ctr': [0.08] * len(test_spend),
        'cvr': [0.05] * len(test_spend)
    })
    preds = model.predict(test_df)
    roi_preds = [round((p * 100) / s, 2) for p, s in zip(preds, test_spend)]

    budget_suggestions = [
        {'spend': s, 'predicted_conversions': int(p), 'predicted_roi': r}
        for s, p, r in zip(test_spend, preds, roi_preds)
    ]

    return {
        'meta_summary': meta_data,
        'shopify_summary': shopify_data,
        'roi': round(roi, 2),
        'recommendations': ['Focus budget on high-performing creatives with better CTR.'],
        'budget_suggestions': budget_suggestions
    }
