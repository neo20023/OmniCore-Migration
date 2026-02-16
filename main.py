from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import os

# Initialize FastAPI application
app = FastAPI(
    title="OmniCore API",
    description="Multi-Model AI Application Backend",
    version="1.0.0",
    debug=os.getenv("DEBUG", "False").lower() == "true"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "OmniCore Backend is running"}

@app.post("/api/models/web-generator")
async def web_generator(prompt: dict):
    try:
        return {"status": "success", "data": {"message": "Web generation in progress"}}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/models/flutter-generator")
async def flutter_generator(prompt: dict):
    try:
        return {"status": "success", "data": {"message": "Flutter app generation in progress"}}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/models/pcb-designer")
async def pcb_designer(prompt: dict):
    try:
        return {"status": "success", "data": {"message": "PCB design in progress"}}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/models/image-video-generator")
async def image_video_generator(prompt: dict):
    try:
        return {"status": "success", "data": {"message": "Image/Video generation in progress"}}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/models/invention-ai")
async def invention_ai(prompt: dict):
    try:
        return {"status": "success", "data": {"message": "Invention brainstorming in progress"}}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.on_event("startup")
async def startup_event():
    print("🚀 OmniCore Backend is starting...")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)