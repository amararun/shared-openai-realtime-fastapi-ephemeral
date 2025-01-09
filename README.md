# AI API Proxy & OpenAI Realtime Session Manager

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange.svg)](https://openai.com/)
[![Gemini](https://img.shields.io/badge/Google-Gemini-blue.svg)](https://deepmind.google/technologies/gemini/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A FastAPI application that provides:
- OpenAI's realtime session API for voice interactions
- OpenAI chat completion proxy endpoint
- Google Gemini chat completion proxy endpoint

## 🚀 Setup

1. Clone this repository
2. Create a `.env` file based on `.env_example` and add your API keys:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `GEMINI_API_KEY`: Your Google Gemini API key
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Running the App

Start the server locally:
```bash
uvicorn app:app --reload
```

The server will start at `http://localhost:8000`

## 🌐 Deployment

This application can be deployed on various platforms including:
- Render
- Railways
- AWS Lambda
- Other web services of your choice

### 🔨 Build Command
To install the required dependencies:
```bash
pip install -r requirements.txt
```

### ⚡ Run Command
To start the server in production:
```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

## 🔌 API Endpoints

### GET /session

Creates a new realtime session with OpenAI.

Query Parameters:
- `model`: The OpenAI model to use
- `voice`: The voice to use for the session

Example:
```
GET /session?model=gpt-4&voice=alloy
```

### POST /open-chat-completion

Proxy endpoint for OpenAI's chat completion API.

Request Body:
```json
{
    "model": "gpt-4",
    "messages": [
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "temperature": 0.7
}
```

### POST /gemini-chat-completion

Proxy endpoint for Google's Gemini chat completion API.

Request Body:
```json
{
    "model": "gemini-1.5-flash",  // Optional, defaults to gemini-1.5-flash
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "Hello, how are you?"
                }
            ]
        }
    ]
}
```

## ⚙️ Environment Variables

Required API keys in your `.env` file:
- `OPENAI_API_KEY`: Your OpenAI API key
- `GEMINI_API_KEY`: Your Google Gemini API key

## 🔒 CORS Configuration

By default, the server accepts requests from all origins (`*`). To restrict access to specific domains, modify the CORS middleware configuration in `app.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yourdomain.com",
        "https://your-subdomain.yourdomain.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
```

Adjust the `allow_origins` list according to your security requirements. 