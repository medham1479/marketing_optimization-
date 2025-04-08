# 📈 AI-Powered Marketing Optimization Platform

A full-stack AI-driven dashboard that integrates Meta Ads data and Shopify sales insights to deliver automated ROI analysis and intelligent ad spend recommendations.


## 🧠 Tech Stack

| Layer       | Stack                           |
|-------------|----------------------------------|
| Frontend    | HTML, CSS, JavaScript, Chart.js  |
| Backend     | Python, Flask, scikit-learn      |
| Data Models | Pandas, LinearRegression         |
| Infra       | Docker, Docker Compose, Nginx    |

---

## 🗂️ Project Structure

```
marketing-optimization-platform/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── services/
│   │   ├── meta_service.py
│   │   └── shopify_service.py
│   └── models/
│       └── insights.py
├── frontend/
│   ├── Dockerfile
│   └── index.html
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup & Run Instructions

> 🐳 Prerequisite: Docker installed → https://docs.docker.com/get-docker/

### 1. Clone the repository
```bash
git clone https://github.com/your-username/marketing-optimization-platform.git
cd marketing-optimization-platform
```

### 2. Start the app
```bash
docker-compose up --build
```

### 3. View in browser
- Frontend: http://localhost:3000  
- Backend API: http://localhost:5000/api/insights

-