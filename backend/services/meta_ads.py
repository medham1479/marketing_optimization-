import os
import datetime
import pandas as pd
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta


# Try importing Meta Ads SDK
try:
    from facebook_business.api import FacebookAdsApi
    from facebook_business.adobjects.adaccount import AdAccount
    from facebook_business.adobjects.adsinsights import AdsInsights
except ImportError:
    FacebookAdsApi = None  # fallback

load_dotenv()

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
AD_ACCOUNT_ID = os.getenv("META_AD_ACCOUNT_ID")

def get_meta_ads_data():
    """
    Attempts to pull real Meta Ads data if credentials and SDK are available.
    Otherwise returns structured mock data.
    """
    if not ACCESS_TOKEN or not AD_ACCOUNT_ID or FacebookAdsApi is None:
        print("⚠️ Meta Ads credentials missing. Returning mock data.")
        return get_mock_meta_ads_data()

    FacebookAdsApi.init(access_token=ACCESS_TOKEN)

    try:
        fields = [
            AdsInsights.Field.campaign_name,
            AdsInsights.Field.date_start,
            AdsInsights.Field.impressions,
            AdsInsights.Field.clicks,
            AdsInsights.Field.conversions,
            AdsInsights.Field.spend,
        ]
        params = {
            'level': 'campaign',
            'time_range': {
                'since': (datetime.date.today() - datetime.timedelta(days=30)).isoformat(),
                'until': datetime.date.today().isoformat()
            }
        }

        ads = AdAccount(AD_ACCOUNT_ID).get_insights(fields=fields, params=params)
        return [dict(ad) for ad in ads]

    except Exception as e:
        print(f" Error calling Meta API: {e}")
        return get_mock_meta_ads_data()

def get_mock_meta_ads_data():
    """
    Returns mock ad campaign data in the same structure as Meta Ads API.
    """
    campaigns = ["Campaign A", "Campaign B"]
    variants = ["A", "B"]
    today = datetime.today()

    data = []

    for i in range(30):  # last 30 days
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        for campaign in campaigns:
            for variant in variants:
                impressions = random.randint(1000, 5000)
                clicks = random.randint(100, impressions)
                conversions = random.randint(10, clicks)
                spend = round(random.uniform(50, 300), 2)

                data.append({
                    "campaign": campaign,
                    "variant": variant,
                    "date": date,
                    "impressions": impressions,
                    "clicks": clicks,
                    "conversions": conversions,
                    "spend": spend
                })

    return data