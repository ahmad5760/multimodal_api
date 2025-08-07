import os
from openai import OpenAI
from fastapi import UploadFile, HTTPException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
# It's recommended to handle the API key securely, e.g., via environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def transcribe_audio(file: UploadFile):
    """
    Transcribes an audio file using OpenAI's Whisper model.
    """
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an audio file.")

    try:
        # The openai library can directly handle the file-like object from UploadFile
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=file.file, # Pass the underlying file-like object
            response_format="json"
        )
        return transcription.text
    except Exception as e:
        # Handle potential API errors or other issues
        raise HTTPException(status_code=500, detail=f"Failed to transcribe audio: {str(e)}")