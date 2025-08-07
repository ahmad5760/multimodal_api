from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from app.services import tts_service

router = APIRouter()

class TTSRequest(BaseModel):
    text: str

@router.post("/tts", tags=["Text-to-Speech"])
async def create_tts(request: TTSRequest):
    """
    Converts a given text input into a synthesized audio file.
    - **text**: The text to be converted to speech.
    """
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    audio_bytes = await tts_service.synthesize_speech(request.text)
    
    # Return the audio file as a downloadable response
    return Response(content=audio_bytes, media_type="audio/wav", headers={
        "Content-Disposition": "attachment; filename=synthesized_speech.wav"
    })