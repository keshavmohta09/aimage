"""
This file contains stability ai sdk
"""

import base64
import json
from typing import Optional

import requests
from django.conf import settings
from django.core.files.base import ContentFile

from utils.stabilityai_sdk.constants import NO_ARTIFACTS_FOUND_IN_RESPONSE
from utils.stabilityai_sdk.exceptions import StabilityAIException


class StabilityAISDK:
    BASE_URL = settings.STABILITY_AI_BASE_URL
    API_KEY = settings.STABILITY_AI_API_KEY

    def __init__(self, api_key: Optional[str] = None):
        if api_key:
            self.API_KEY = api_key

    def _get_headers(self):
        """
        Returns the headers for the API request.
        """
        return {
            "authorization": f"Bearer {self.API_KEY}",
            "accept": "application/json",
            "content-type": "application/json",
        }

    def generate_sd_xl_image(self, prompt: str) -> ContentFile:
        """
        Generates a stable-diffusion-xl image based on the provided text prompt.
        """
        response = requests.post(
            url=f"{self.BASE_URL}/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
            headers=self._get_headers(),
            data=json.dumps({"text_prompts": [{"text": prompt}]}),
        )

        if response.status_code != 200:
            raise StabilityAIException(
                message=f"Error {response.status_code}: {response.text}"
            ) from None

        try:
            data = response.json()
        except json.JSONDecodeError as error:
            raise StabilityAIException(message=str(error)) from error

        if "artifacts" not in data or len(data["artifacts"]) < 1:
            raise StabilityAIException(message=NO_ARTIFACTS_FOUND_IN_RESPONSE) from None

        images = data["artifacts"]
        content_files = []
        for index, image in enumerate(images):
            image_data = base64.b64decode(image["base64"])
            content_file = ContentFile(image_data, name=f"{prompt}-{index}.png")
            content_files.append(content_file)

        return content_files[0]
