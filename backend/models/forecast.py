import pandas as pd
from prophet import Prophet

def generate_forecast(meta_data):
    df = pd.DataFrame(meta_data)

    if 'date' not in df.columns or 'conversions' not in df.columns:
        return []

    daily = df.groupby('date').sum().reset_index()[['date', 'conversions']]
    daily.columns = ['ds', 'y']

    if daily.empty:
        return []

    model = Prophet()
    model.fit(daily)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat']].tail(7).to_dict(orient='records')
