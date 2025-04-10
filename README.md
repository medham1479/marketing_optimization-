# 📈 AI-Powered Marketing Optimization Dashboard

This is a proof-of-concept full-stack platform to analyze and optimize Meta Ads + Shopify performance using AI (LLMs), statistical analysis (Z-tests), and time-series forecasting (Prophet). It provides real-time insights, recommendations, and visual dashboards based on ad and ecommerce data.

---

##  Features

###  1. Meta Ads + Shopify Integration
- Pulls **simulated Meta Ads** and **Shopify sales** data.
- Users can toggle between **mock data** or plug in **real API keys** (Meta Ads & Shopify APIs supported).
- Meta Ads data includes spend, impressions, clicks, conversions, variants (A/B).
- Shopify data includes product, sales, revenue, etc.

### 2. AI-Powered Recommendations (OpenAI + OpenLLM)
- Uses **OpenAI GPT-4** (or any LLM via OpenLLM) to analyze ad performance metrics.
- Generates natural-language recommendations such as:
  - Which ad creative performs better.
  - Whether to shift budget.
  - Suggestions for targeting/landing pages.

###  3. Real-Time Web Dashboard (Frontend)
- Built with **HTML + Chart.js + JS + Docker + Flask backend**.
- Visualizes:
  -  Forecasted conversions (7-day Prophet model).
  -  Revenue by product.
  -  A/B test results & CTR comparison.
  - AI recommendations.
- Auto-refreshes every **10 seconds** to simulate real-time updates.



##  Project Structure

```
.
├── main.py                   # Flask backend entry point
├── meta_ads.py               # Simulated + real Meta Ads data loader
├── shopify_data.py           # Simulated Shopify sales data
├── models/
│   ├── insights.py           # AI + analytics logic for recommendations
│   ├── forecast.py           # Prophet-based conversion forecasts
│   └── ab_test.py            # Z-test logic for A/B comparison
├── static/
│   └── index.html            # Frontend dashboard (Chart.js, live updates)
├── Dockerfile + docker-compose.yml
├── requirements.txt
└── .env                      # API keys, tokens, etc.
```

---

##  Setup Instructions

1. **Clone and Build:**

```bash
git clone https://github.com/your-username/marketing_optimization.git
cd marketing_optimization
docker-compose up --build
```

2. **Add `.env`:**

```env
OPENAI_API_KEY=your_openai_key
META_ACCESS_TOKEN=optional_meta_access_token
SHOPIFY_API_KEY=optional_key
SHOPIFY_PASSWORD=optional_pw
```

3. **Visit:**  
Open `http://localhost:3000` in your browser to view the dashboard.

---


---

## 📈 Dashboard Highlights

| Section                    | What It Shows                                             |
|----------------------------|-----------------------------------------------------------|
| KPI Cards                  | Total ROI, Spend, Revenue                                 |
| Forecasted Conversions     | 7-day prediction via Prophet                              |
| Shopify Revenue by Product | Bar chart of revenue by product                           |
| A/B Test Results           | CTR, conversions, impressions for variant A vs B          |
| AI Recommendations         | Natural-language summary of ad trends and suggestions     |
| Filters                    | Dropdown to view metrics by campaign (A, B, or All)       |

---

## Technical Architecture

This platform follows a modular, full-stack architecture with machine learning, AI-powered data simulation, backend logic, and frontend visualization:


                        +------------------------------+
                        |    Meta Ads (Real API)       |
                        |        or                    |
                        |  🤖 AI-Generated Meta Data    |
                        |  (via OpenAI/OpenLLM)        |
                        +--------------+---------------+
                                       |
                                       v
                        +------------------------------+
                        |        Backend (Flask)        |
                        |  - /api/insights              |
                        |  - /api/abtest                |
                        |  - /api/forecast              |
                        +--------------+---------------+
                                       |
         +-----------------------------+------------------------------+
         |                                                            |
         v                                                            v
+-----------------------------+                        +-----------------------------+
|     AI/ML Services         |                        |     Shopify API/Meta API (or|
| - Forecasting (Prophet)     |                        |     AI-generated Data)      |
| - A/B Testing (Z-Test)      |                        +-----------------------------+
| - Insights + Recommendations|
|   (Open AI)                  |
+--------------+--------------+
               |
               v
+---------------------------------------------------+
|   Frontend (HTML/CSS/JS + Chart.js)               |
| - KPI Cards                                       |
| - Forecasted Conversions Chart                    |
| - Revenue by Product Chart                        |
| - A/B Test Results (with CTR/Spend metrics)       |
| - AI-Generated Recommendations                    |
| - Campaign Filter Dropdown                        |
+---------------------------------------------------+

```

- **Meta Ads AI Layer**: If no API key is present, the system uses OpenAI/OpenLLM to generate realistic ad performance data (impressions, clicks, spend, CTR, etc.).
- **AI Integration**: All major decisions (recommendations, data simulation) are powered by LLMs for smarter automation.
- **Modular Backend**: Flask handles all routing and data processing, dynamically using real or simulated data.
- **Frontend Dashboard**: Real-time charts and insights update every 10s for a live view of marketing performance.

---

## Technologies Used

- Flask + Python
- Prophet (Facebook)
- OpenAI GPT-3.5 + OpenLLM
- Chart.js (Frontend)
- Docker + Docker Compose

---

##  Security

- API Keys stored securely in `.env`
- Never committed to version control
- All external requests sanitized

---

##  Testing

Run:

```bash
docker-compose exec backend pytest
```

---

## Notes

- All data is simulated unless real tokens are configured.


---
Created by: Medha Mamidipaka | mmami@illinois.edu