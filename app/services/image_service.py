import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

# Use the new v2beta API endpoint
STABILITY_API_HOST = "https://api.stability.ai"
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

if not STABILITY_API_KEY:
    raise Exception("Missing Stability AI API key.")

async def generate_image_from_prompt(prompt: str, aspect_ratio: str = "1:1", output_format: str = "png"):
    """
    Generates an image from a text prompt using Stability AI's v2beta API.
    Returns the image content as bytes.
    """
    api_url = f"{STABILITY_API_HOST}/v2beta/stable-image/generate/core"

    headers = {
        # The API key is sent in the Authorization header
        "authorization": f"Bearer {STABILITY_API_KEY}",
        # We are accepting an image in response
        "accept": "image/*"
    }

    # This is a multipart/form-data request, so we use 'data' and 'files'
    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "output_format": output_format,
    }
    
    # The 'requests' library will automatically set the Content-Type to multipart/form-data
    # The `files` parameter is required, even if empty, as per Stability AI's documentation
    files = {"none": ''}

    try:
        response = requests.post(api_url, headers=headers, files=files, data=payload)

        # Check for successful response
        if response.status_code == 200:
            # The response content is the raw image bytes
            return response.content
        else:
            # If not successful, raise an exception with the error details from the API
            response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle network errors or non-200 responses
        error_details = "Unknown error"
        try:
            # Try to parse the JSON error response from Stability AI
            error_details = e.response.json()
        except:
            # If the response isn't JSON, use the raw text
            error_details = e.response.text if e.response else "No response from server"
            
        raise HTTPException(
            status_code=e.response.status_code if e.response else 503,
            detail=f"Stability AI API request failed: {error_details}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")