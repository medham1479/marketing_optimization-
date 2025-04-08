import random
import datetime

def get_meta_ads_data():
    campaigns = ['Campaign A', 'Campaign B']
    data = []

    for i in range(30):
        date = (datetime.date.today() - datetime.timedelta(days=29 - i)).isoformat()
        for campaign in campaigns:
            spend = round(random.uniform(100, 300), 2)
            impressions = random.randint(1000, 5000)
            clicks = random.randint(100, impressions)  # <= clicks ≤ impressions
            conversions = int(clicks * random.uniform(0.1, 0.3))
            variant = random.choice(['A', 'B'])

            data.append({
                'date': date,
                'campaign': campaign,
                'spend': spend,
                'impressions': impressions,
                'clicks': clicks,
                'conversions': conversions,
                'variant': variant
            })

    return data
