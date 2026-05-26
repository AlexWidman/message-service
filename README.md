# Message Service API

A REST API for sending, retrieving, and deleting messages built with FastAPI and SQLite.

## Features

- Send messages to recipients
- Fetch unread messages for a recipient
- Fetch all messages for a recipient (ordered by timestamp)
- Fetch all messages stored in the database (ordered by timestamp)
- Delete single message
- Delete multiple messages

## Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite

## Setup

### Clone repository

```bash
git clone https://github.com/AlexWidman/message-service
cd message_service
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### Activate virtual environment (macOS / Linux)

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

## Swagger Documentation

Swagger UI is available at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create message

```http
POST /messages
```

### Fetch unread messages

```http
GET /messages/unread/{recipient}
```

### Fetch all messages

```http
GET /messages
```

### Fetch messages for recipient

```http
GET /messages/{recipient}
```

### Delete single message

```http
DELETE /messages/{message_id}
```

### Delete multiple messages

```http
DELETE /messages
```

## Assumptions

- Messages are plain text only
- Authentication/authorization is intentionally omitted
- Fetching unread messages marks them as read
- Timestamps are stored in UTC