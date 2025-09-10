# Celery + RabbitMQ POC

This repository contains a small Proof of Concept (POC) for integrating **Celery** with **RabbitMQ** to handle asynchronous task scheduling and execution. The setup includes **FastAPI**, **Celery Worker**, **Celery Beat**, and **RabbitMQ** for messaging.

---

## Features

* Schedule tasks using **Celery Beat**
* Execute tasks asynchronously with **Celery Worker**
* Reliable task distribution via **RabbitMQ**
* Real-time UI updates and database persistence (PostgreSQL)
* Fully containerized using **Docker** and **Docker Compose**

---

## Repository Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
├── run_task.py
├── tasks/
│   ├── __init__.py
│   ├── workers.py
│   └── compute.py
└── .gitignore
```

---

## Getting Started

### Prerequisites

* Docker & Docker Compose installed
* Python 3.10+ (for local testing, optional)

### Running with Docker Compose

1. Build and start all services:

```bash
docker-compose up --build
```

2. Access services:

* FastAPI app: [http://localhost:8000](http://localhost:8000)
* RabbitMQ Management UI: [http://localhost:15672](http://localhost:15672)
  (Username: `guest`, Password: `guest`)

---

### Running Tasks Locally

To test tasks locally without Docker:

```bash
pip install -r requirements.txt
python run_task.py
```

---

## How It Works

1. **Automatic Session Trigger** → Celery Beat schedules the task.
2. **Celery Worker** picks up the scheduled job.
3. **RabbitMQ** handles messaging:

   * Sends **UI Response** to update the interface in real-time.
   * Sends **Database Response** to persist results in PostgreSQL.
4. Celery Beat + Worker + RabbitMQ ensure reliable and distributed task execution.

---

## Example Tasks

* `add(x, y)` → Adds two numbers asynchronously.
* `process_data(data)` → Performs heavy computation and sends results to frontend & DB.

---

## Notes

* `.gitignore` ensures virtual environments, `__pycache__`, and Celery Beat schedule files are not tracked.
* No sensitive information is included in this repo.

---

## License

This project is for demonstration purposes. You may modify or use it internally as needed.
