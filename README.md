# AidSense 🌍🧠  
**Multimodal AI System for Real-Time Disaster Detection and Response**

AidSense is an advanced open-source AI platform that integrates satellite fire data, social media intelligence, and geospatial analytics to provide real-time monitoring, analysis, and early warnings for natural disasters. It combines multimodal signal fusion with interactive visualization to support faster and smarter disaster response.

---

## 🔍 Key Features

- 🔥 **Satellite Fire Detection**: Fetches and visualizes NASA FIRMS fire points in near real time.
- 📡 **Social Media Intelligence**: Parses disaster-related tweets and Telegram updates to detect local reports.
- 🧠 **Multimodal Signal Fusion** *(in development)*: Combines multiple data sources for anomaly detection.
- 🗺️ **Geospatial Visualization**: Interactive Mapbox maps with layered visual feedback.
- 🌐 **Web-Based Dashboard**: Streamlit-powered real-time dashboard.

---

## 📁 Project Structure

AidSense/
├── web_demo/
│ └── app.py # Streamlit dashboard for live visualization
├── data/ # NASA CSV fire data (downloaded or auto-fetched)
├── .env # API keys (NASA, Twitter, etc.)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- NASA API Key (https://firms.modaps.eosdis.nasa.gov/)
- Twitter Developer Token (optional)
- Telegram Bot Token (optional)

### ▶️ Run the app

```bash
pip install -r requirements.txt
streamlit run web_demo/app.py
NASA_API_KEY=your_nasa_api_key_here
TWITTER_BEARER_TOKEN=your_token_here
TELEGRAM_BOT_TOKEN=your_token_here
🧠 愿景
AidSense 旨在展示人工智能和开放数据如何通过智能整合天基和地面观测数据，加速灾害响应。它可扩展用于野火预警系统、洪水监测或地震警报。

📜 许可证
MIT 许可证 — 可免费使用、共享和修改（需注明出处）。

🤝 贡献
欢迎大家贡献力量！您可以提交功能创意、错误报告或拉取请求，以改进此平台，使其更具全球影响力。
作者： chenshisan111
合作或支持：cshisan66@gmail.com
