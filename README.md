# Serafim - Surveillance platform

Serafim is a modular system for realtime surveillance. The platform combines a backend API with a frontend dashboard that presents system status, logs and events. 

Serafim is developed with a focus on: 
- Stability
- Security
- Observability

## Functionality 
- Backend (FastAPI and Uvicorn)
- Frontend (HTML/JS/CSS)

## Technical structure
serafim/
├── backend/
│   ├── main.py
│   ├── logs/
│   │   └── serafim.log
│   ├── services/
│   │   └── log_pipeline.py
│   └── systemd/
│       └── serafim.service
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── README.md

## Installation
1. Clone repo:

```
git clone https://github.com/<user>/serafim.git
cd serafim
```

2. Install backend dependencies

```
pip install -r requirements.txt 
```

3. 

``` 
uvicorn backend.main:app --reload 
```

4.  Open frontend/index.html in browser

(to be continued) 
