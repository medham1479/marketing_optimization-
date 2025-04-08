import random

def get_meta_ads_data():
    campaigns = ['Spring Sale', 'Summer Blast', 'Flash Promo', 'Back to School', 'Holiday Blitz']
    data = []

    for _ in range(5):
        name = random.choice(campaigns)
        spend = round(random.uniform(100, 1000), 2)
        impressions = random.randint(5000, 50000)
        ctr = random.uniform(0.03, 0.15)
        clicks = int(impressions * ctr)
        cvr = random.uniform(0.02, 0.12)
        conversions = int(clicks * cvr)

        data.append({
            'campaign': name,
            'spend': spend,
            'impressions': impressions,
            'clicks': clicks,
            'conversions': conversions
        })

    return data
