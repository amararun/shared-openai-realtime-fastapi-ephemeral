from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Add CORS middleware with permissive settings for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://tigzig.com",
        "https://realtime.tigzig.com",
        "https://rex.tigzig.com",
        "https://rexrc.tigzig.com",
        "https://mf.tigzig.com",
        "http://localhost:8000"   # For local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/session")
async def get_session(
    model: str = Query(..., description="The model to use"),
    voice: str = Query(..., description="The voice to use")
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/realtime/sessions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "voice": voice,
                 "temperature": 0.6,
                 "turn_detection": {
                        "type": "server_vad",
                        "threshold": 0.7
                 }
                 
            }
        )
        
        return response.json()

@app.post("/open-chat-completion")
async def proxy_chat_completion(request_body: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                "Content-Type": "application/json"
            },
            json=request_body
        )
        return response.json()

@app.post("/gemini-chat-completion")
async def gemini_chat_completion(request_body: dict):
    async with httpx.AsyncClient() as client:
        API_KEY = os.getenv('GEMINI_API_KEY')
        model = request_body.get("model", "gemini-1.5-flash")  # Default to gemini-1.5-flash if not provided
        response = await client.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}",
            headers={
                "Content-Type": "application/json"
            },
            json=request_body
        )
        return response.json()

# To run the app, use:
# uvicorn app:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))