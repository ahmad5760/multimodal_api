# Mod 7: Multimodal AI Inference APIs using FastAPI

This project is a modular, production-ready FastAPI application that exposes three core multimodal AI services through RESTful APIs: Speech-to-Text, Text-to-Speech, and Image Generation.

## Features

- **Speech-to-Text (STT)**: Convert spoken audio into text using OpenAI's Whisper model.
- **Text-to-Speech (TTS)**: Synthesize speech from text using OpenAI's TTS model.
- **Image Generation**: Generate images from text prompts using Stability AI's Stable Diffusion model.

## Project Structure

```
multimodal_api/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── stt.py
│   │   ├── tts.py
│   │   └── image_gen.py
│   └── services/
│       ├── stt_service.py
│       ├── tts_service.py
│       └── image_service.py
│
├── requirements.txt
├── .env
└── README.md
```

## Setup and Installation

### 1. Prerequisites
- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Stability AI API key](https://platform.stability.ai/account/keys)

### 2. Clone the Repository
```bash
git clone <your-repo-url>
cd multimodal_api
```

### 3. Create a Virtual Environment
It's highly recommended to use a virtual environment.
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the project root directory and add your API keys:
```
OPENAI_API_KEY="your_openai_api_key_here"
STABILITY_API_KEY="your_stability_api_key_here"
```

## Running the Application

To run the FastAPI server, use `uvicorn`. The `--reload` flag enables auto-reloading when you make changes to the code.
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## API Usage (cURL Examples)

### 1. POST /stt (Speech-to-Text)
Converts an audio file to text. Replace `/path/to/your/audio.mp3` with the actual path to your audio file.

```bash
curl -X POST "http://127.0.0.1:8000/stt" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@/path/to/your/audio.mp3;type=audio/mpeg"
```
**Response:**
```json
{
  "transcription": "Your transcribed text appears here."
}
```

### 2. POST /tts (Text-to-Speech)
Converts text to an audio file. The response will be a `.wav` file. Use `-o` to save it.

```bash
curl -X POST "http://127.0.0.1:8000/tts" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"text": "Hello, this is a test of the text to speech API."}' \
-o output_speech.wav
```
This will save the synthesized audio as `output_speech.wav` in your current directory.

### 3. POST /generate-image (Image Generation)
Generates an image from a text prompt. The response is a `.png` image. Use `-o` to save it.

```bash
curl -X POST "http://127.0.0.1:8000/generate-image" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"prompt": "A majestic lion wearing a crown, studio lighting, hyperrealistic"}' \
-o generated_image.png
```
This will save the generated image as `generated_image.png` in your current directory.