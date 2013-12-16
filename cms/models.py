from django.db import models

# models
from base.models import BaseModel


class Interview(BaseModel):
    def file_path(self, name):
        """ file path for the file obj """
        return "%s" % name

    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        unique=True, null=True, blank=True,
    )
    summary = models.TextField(
    )
    who_you_are = models.TextField(
    )
    what_hardware = models.TextField(
    )
    what_software = models.TextField(
    )
    dream_setup = models.TextField(
    )
    picture = models.ImageField(
        upload_to=file_path, null=True, blank=True,
    )

    image_sizes = [(265, 170)]

    #public methods
    def save(self, *args, **kwargs):
        """
        Interview save method, overriden to set the picture size
        """

        super(Interview, self).save(*args, **kwargs)
        try:
            self._process_image('picture')
        except:
            pass
