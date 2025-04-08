import pandas as pd
import math
from statsmodels.stats.proportion import proportions_ztest

def run_ab_test(meta_data):
    df = pd.DataFrame(meta_data)

    if 'variant' not in df.columns:
        return { "error": "Missing 'variant' column in ad data." }

    grouped = df.groupby('variant').agg({
        'impressions': 'sum',
        'clicks': 'sum',
        'conversions': 'sum',
        'spend': 'sum'
    })

    if 'A' not in grouped.index or 'B' not in grouped.index:
        return { "error": "Both variant A and B are required for A/B testing." }

    conversions = grouped['conversions']
    trials = grouped['spend']

    # Perform proportions z-test on conversions / spend
    try:
        z_stat, p_val = proportions_ztest(count=conversions, nobs=trials)
    except Exception as e:
        p_val = None

    variant_stats = []
    for variant in ['A', 'B']:
        stats = grouped.loc[variant]
        variant_stats.append({
            "variant": variant,
            "impressions": int(stats.impressions),
            "clicks": int(stats.clicks),
            "conversions": int(stats.conversions),
            "ctr": stats.clicks / stats.impressions if stats.impressions else 0,
            "spend": float(stats.spend)
        })

    return {
        "variant_stats": variant_stats,
        "p_value": round(float(p_val), 4) if p_val is not None and not math.isnan(p_val) else None,
        "interpretation": (
            "Variant A significantly outperforms B" if p_val is not None and p_val < 0.05
            else "No statistically significant difference between A and B"
        )
    }
