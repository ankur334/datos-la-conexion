from django.db import models


# Create your models here.
from connections.utils import upload_location, validate_file


class Data(models.Model):
    """
    # TODO:: Write documentation for it.
    """
    name = models.CharField(max_length=255)
    table_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class File(models.Model):
    """
    # TODO:: Write documentation for it
    """
    name = models.CharField(max_length=999, blank=False)
    display_name = models.CharField(max_length=999, blank=False)
    type = models.CharField(max_length=20, blank=False)
    file = models.FileField(
        upload_to=upload_location,
        validators=[validate_file],
        null=False,
        blank=False,
        max_length=1000
    )