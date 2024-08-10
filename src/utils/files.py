"""
This file contains all the utils related to files
"""

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible

FILE_STORAGE = FileSystemStorage(location=settings.BASE_DIR)


@deconstructible
class RenameFile:
    def __init__(self, pattern):
        self.pattern = pattern

    def __call__(self, instance, filename):
        extension = filename.split(".")[-1]
        return self.pattern.format(instance=instance, extension=extension)
