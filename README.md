#  AI-Powered Marketing Optimization Dashboard

A full-stack analytics platform that helps marketing teams explore ad performance, forecast conversions, and generate AI-based recommendations using simulated Meta Ads and Shopify data. Built with Flask (Python backend) and Chart.js (HTML frontend).

---

## Features

### Core Capabilities

- **Ad Performance Analysis**  
  Analyze impressions, spend, clicks, CTR, and conversions from Meta-style ads.

- **Shopify Integration**  
  View revenue by product, total revenue, and purchase behavior.

- **Forecasting**  
  Uses Facebook Prophet to predict future conversions for the next 7 days.

- **A/B Testing**  
  Automatically compares performance between Variant A (video ad) and Variant B (static ad) using z-tests and CTR trends over time.

- **AI Recommendations**  
  Automatically provides natural-language strategy suggestions based on ad performance data and trends.

- **Campaign Filtering**  
  Filter the dashboard by campaign (All, Campaign A, Campaign B) to isolate insights.

- **Live Dashboard**  
  Auto-refreshing charts and KPIs every 10 seconds for real-time updates.

---

##  Dashboard Layout (Frontend Overview)

### Campaign Filter
- Dropdown selector allows filtering by **All**, **Campaign A**, or **Campaign B**.
- Updates all charts and insights dynamically.

###  KPI Summary Cards
- **ROI**: Calculated based on revenue vs spend.
- **Total Spend**: From ad campaign data.
- **Total Revenue**: From Shopify data.

### Charts

- **Forecasted Conversions**  
  Line chart showing the predicted number of conversions for the next 7 days.

- **Revenue by Product**  
  Bar chart displaying revenue breakdown by each product.

- **CTR Over Time (A/B Test)**  
  Line chart comparing daily CTRs between Variant A and Variant B.

- **Predictive Budget ROI**  
  Bar chart showing expected ROI for different budget allocations.

###  A/B Test Results
- Table of impressions, clicks, conversions, and CTR per variant.
- Statistical test results (z-test) with interpretation (e.g., significant or not).

###  AI-Powered Recommendations
- LLM-style text block summarizing suggestions like:
  - Shift more budget to Campaign A.
  - Pause Campaign B if underperforming.
  - Test new creatives if CTR is flat.

---

## 🛠️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/marketing-optimizer.git
cd marketing-optimizer
```

### 2. Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the App



```bash
docker-compose up --build
```

### 4. Open in Browser

Visit [http://localhost:3000]

---

##  Project Structure

```
marketing-optimizer/
├── backend/
│   ├── main.py               # Flask server
│   ├── models/
│   │   ├── insights.py       # Summarization & metrics
│   │   ├── forecast.py       # Prophet model
│   │   ├── ab_test.py        # A/B testing logic
│   │  
│   └── services/
│       ├── meta_ads.py   # Simulated Meta Ads data
│       └── shopify.py# Simulated Shopify data
├── frontend/
│   └── index.html            # Interactive dashboard
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🔌 API Endpoints

| Endpoint         | Description                            |
|------------------|----------------------------------------
| `/api/insights`  | Combined metrics, summaries, AI advice 
| `/api/forecast`  | 7-day conversion forecast               
| `/api/abtest`    | CTR + conversions comparison A vs B    
| `/api/recommendations` | Raw natural language insights     

---

##  Tech Stack

- **Backend**: Python, Flask, pandas, Prophet, statsmodels
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **AI/ML**: Prophet, z-tests, rule-based LLM logic
- **DevOps**: Docker, docker-compose

---



Built by Medha Mamidipaka
mmami@illinois.edu

