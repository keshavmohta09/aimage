"""
This file contains all admins for prompts module.
"""

from django.contrib import admin

from prompts.models import ImagePrompt


@admin.register(ImagePrompt)
class ImagePromptAdmin(admin.ModelAdmin):
    list_display = ("id", "prompt", "image")
    search_fields = ("prompt",)
