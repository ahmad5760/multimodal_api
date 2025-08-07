from fastapi import FastAPI
from app.routes import stt, tts, image_gen

app = FastAPI(
    title="Multimodal AI Inference API",
    description="A FastAPI application for Speech-to-Text, Text-to-Speech, and Image Generation.",
    version="1",
)

# Include the API routers
app.include_router(stt.router)
app.include_router(tts.router)
app.include_router(image_gen.router)

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Multimodal AI Inference API!"}