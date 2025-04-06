# Elderly Care Multi-Agent AI System

A comprehensive AI system designed to assist elderly individuals living independently through a collaborative network of specialized AI agents.

## System Components

1. **Orchestrator Agent**: Coordinates communication between all agents and manages the overall system flow
2. **Health Monitoring Agent**: Tracks vital signs and health metrics
3. **Safety Monitoring Agent**: Detects falls and unusual behavior patterns
4. **Reminder Agent**: Manages medication schedules and daily activities
5. **Communication Agent**: Handles alerts and notifications to caregivers and family members

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with necessary configuration:
```
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=your_database_url
```

4. Run the system:
```bash
python main.py
```

## Project Structure

```
├── agents/
│   ├── orchestrator.py
│   ├── health_monitor.py
│   ├── safety_monitor.py
│   ├── reminder.py
│   └── communication.py
├── models/
│   ├── user.py
│   ├── alert.py
│   └── health_data.py
├── utils/
│   ├── config.py
│   └── helpers.py
├── main.py
├── requirements.txt
└── README.md
```

## Features

- Real-time health monitoring
- Fall detection and emergency alerts
- Medication and activity reminders
- Multi-channel communication (voice, text, app notifications)
- Caregiver dashboard
- Health data analytics 