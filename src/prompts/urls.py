"""
This file contains all the urls related to prompts module
"""

from django.urls import path

from .views import CreateImagePromptAPI

urlpatterns = [
    path("images/", CreateImagePromptAPI.as_view(), name="image-prompts-list"),
]
