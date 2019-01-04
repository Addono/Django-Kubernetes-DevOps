from django.db import models

from sorl.thumbnail import ImageField


class Image(models.Model):
    title = models.CharField(max_length=200, null=False, default="")
    image = ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='tags')
