from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import Response
from app.services import image_service
from typing import Literal

router = APIRouter()


@router.post("/generate-image", tags=["Image Generation"])
async def create_image(
    prompt: str = Form(..., description="The text prompt to generate an image from."),
    aspect_ratio: Literal["16:9", "1:1", "21:9", "2:3", "3:2", "4:5", "5:4", "9:16", "9:21"] = Form(
        "1:1",
        description="The desired aspect ratio (e.g., '16:9', '1:1')."
    ),
    output_format: Literal["jpeg", "png", "webp"] = Form(
        "png",
        description="The desired file format (e.g., 'png', 'jpeg')."
    )
):
    """
    Generates an image from a provided textual prompt using Stability AI.
    This endpoint accepts multipart/form-data.
    """
    if not prompt or not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    # CHANGE 4: Call the service with the direct variables from the form
    image_bytes = await image_service.generate_image_from_prompt(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        output_format=output_format
    )
    
    # CHANGE 5: Use the direct variable for the media type
    media_type = f"image/{output_format}"
    return Response(content=image_bytes, media_type=media_type)