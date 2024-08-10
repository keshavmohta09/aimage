"""
This file contains all the models related to prompts module
"""

from django.core.validators import FileExtensionValidator
from django.db import models

from utils.files import FILE_STORAGE, RenameFile
from utils.models import BaseModel


class ImagePrompt(BaseModel):
    """
    This model is used to store image for a prompt
    """

    EXTENSIONS_ALLOWED = ("jpeg", "png", "jpg")

    prompt = models.TextField(help_text="Stores the prompt provided by the user")
    image = models.ImageField(
        storage=FILE_STORAGE,
        upload_to=RenameFile(
            "files/image_prompt/{instance.prompt}/{instance.date_created}.{extension}"
        ),
        validators=[
            FileExtensionValidator(allowed_extensions=EXTENSIONS_ALLOWED),
        ],
    )

    class Meta:
        verbose_name = "Image Prompt"
        verbose_name_plural = "Image Prompts"
