# Intelligent Tax Assistant

This project aims to develop a web-based chatbot that provides personalized tax filing guidance to users based on their financial information and specific tax laws.

## Directory Structure

/tax-assistant
├── /backend
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app.py
│
├── /frontend
│ ├── Dockerfile
│ ├── requirements.txt
│ └── streamlit_app.py
│
├── /data
│ ├── /raw
│ ├── /processed
│ └── /annotations
│
├── /docs
│ └── README.md
│
└── docker-compose.yml


## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Shailabh8/tax-assistant.git
cd tax-assistant

## Run the services using docker compose
docker-compose up --build

## Access the application
Frontend (Streamlit) at http://localhost:8501
Backend (Flask) at http://localhost:5000
