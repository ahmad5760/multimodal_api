from fastapi import APIRouter, File, UploadFile, HTTPException
from pydantic import BaseModel
from app.services import stt_service

router = APIRouter()

class STTResponse(BaseModel):
    transcription: str

@router.post("/stt", response_model=STTResponse, tags=["Speech-to-Text"])
async def create_stt(file: UploadFile = File(...)):
    """
    Converts an uploaded audio file (speech) into text.
    - **file**: The audio file (.wav, .mp3, etc.) to transcribe.
    """
    # Check for a valid file
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded.")
    
    # Supported content types (you can expand this list)
    if file.content_type not in ["audio/wav", "audio/mpeg", "audio/x-wav"]:
         print(f"Warning: Unexpected content type '{file.content_type}'. Processing anyway.")

    transcription_text = await stt_service.transcribe_audio(file)
    return {"transcription": transcription_text}