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

## How to use the API

Here, PowerShell commands are provided for using the API, however, this can be applied to curl, etc.

Base URL:

```text
http://127.0.0.1:8000
```

### Create Message

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages" `
-Method POST `
-ContentType "application/json" `
-Body '{"sender":"bobina","recipient":"bob","content":"COME HOME NOW"}'
```

### Fetch Unread Messages

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages/unread/bob"
```

### Fetch All Messages

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages"
```

### Fetch Messages with index for start and stop

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages?start=0&stop=5"
```

### Fetch messages for a Recipient

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages/bob"
```

### Delete a Message

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages/1" `
-Method DELETE
```

### Delete Multiple Messages

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:8000/messages?message_ids=1&message_ids=2" `
-Method DELETE
```

## Assumptions

- Messages are plain text only
- Authentication/authorization is intentionally omitted
- Fetching unread messages marks them as read
- Timestamps are stored in UTC