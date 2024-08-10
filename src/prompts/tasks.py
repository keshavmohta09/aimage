"""
This file contains all the tasks related to prompts module
"""

from celery import shared_task

from prompts.models import ImagePrompt
from utils.stabilityai_sdk import StabilityAISDK


@shared_task()
def generate_stability_ai_sd_xl_image(prompt: str) -> None:
    """
    This background task is used to generate standard-diffusion-xl image from
    given prompt and save in ImagePrompt model.
    """

    image = StabilityAISDK().generate_sd_xl_image(prompt=prompt)

    image_prompt = ImagePrompt(prompt=prompt, image=image)
    image_prompt.save()
