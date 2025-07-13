# AidSense: Multimodal Disaster Response AI System

## Project Overview

AidSense is an open-source AI system that integrates satellite imagery, real-time social media signals, and large language models (LLMs) to provide timely disaster alerts and response recommendations.

This system empowers communities, NGOs, and governments with early intelligence during natural disasters such as earthquakes, floods, and wildfires.

## Key Features

- **Multimodal Input Pipeline**:  
  - Satellite imagery from NASA FIRMS and Sentinel-2  
  - Real-time data from Twitter and Telegram via keyword and location filters  
  - Newswire and RSS feeds for breaking incident reports

- **Advanced AI Stack**:  
  - YOLOv9 and Segment Anything Model (SAM) for disaster detection on satellite images  
  - Fine-tuned LLaMA-3 or Mistral models for semantic text parsing  
  - Prompt chaining for risk assessment and recommended actions

- **Multilingual Alert Generation**:  
  - Supports English, Swahili, Hindi, French, and other languages  
  - Generates both short social media style alerts and longer PDF reports

- **Interactive Web Dashboard**:  
  - Built with Streamlit and Leaflet.js  
  - Visualizes active disaster zones and AI-generated assessments on maps

## Technology Stack

- PyTorch, HuggingFace Transformers  
- YOLOv9, Segment Anything Model (SAM)  
- LLaMA-3 or Mistral large language models  
- Streamlit for frontend visualization  
- Data APIs from NASA, USGS, EUMETSAT, Twitter

## Project Structure

AidSense/
├── models/ # AI model scripts for image and text processing
├── data/ # Sample satellite images and social text data
├── web_demo/ # Streamlit-based web interface
├── api/ # Optional REST API backend
├── utils/ # Data ingestion and preprocessing scripts
├── .env.template # Template for environment variables (API keys)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── LICENSE # Open-source license
└── architecture.png # System architecture diagram


## Use Cases

- Real-time alerts for disaster-affected communities  
- Coordination tools for NGOs and aid organizations  
- Emergency dashboards for government agencies  
- Media verification of disaster events  

## Contribution and License

AidSense is an open-source project licensed under the MIT License. Contributions and feedback are welcome!
