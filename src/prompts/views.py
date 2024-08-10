from celery import group
from rest_framework import serializers
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from prompts.tasks import generate_stability_ai_sd_xl_image
from utils.constants import REQUEST_HAS_BEEN_PROCESSED
from utils.response import ApiResponse


class CreateImagePromptAPI(APIView):
    class InputSerializer(serializers.Serializer):
        prompt = serializers.CharField(max_length=500)

    def post(self, request, *args, **kwargs):
        # Validate the input prompt using the serializer
        serializer = self.InputSerializer(data=request.data)
        if not serializer.is_valid():
            return ApiResponse(errors=serializer.errors, status=HTTP_400_BAD_REQUEST)

        prompt = serializer.validated_data["prompt"]

        # Trigger the background tasks to generate 3 images in parallel
        image_tasks = group(
            generate_stability_ai_sd_xl_image.s(prompt) for _ in range(3)
        )
        image_tasks.apply_async()

        return ApiResponse(data=REQUEST_HAS_BEEN_PROCESSED, status=HTTP_200_OK)
