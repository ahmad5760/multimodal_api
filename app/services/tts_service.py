import os
from openai import OpenAI
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def synthesize_speech(text: str):
    """
    Synthesizes speech from text using OpenAI's TTS model.
    Returns the audio content as bytes.
    """
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",  # You can choose other voices like: 'nova', 'echo', 'fable', 'onyx', 'shimmer'
            input=text,
        )
        # The response object has a `read()` method that returns the audio bytes
        audio_bytes = response.read()
        return audio_bytes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to synthesize speech: {str(e)}")