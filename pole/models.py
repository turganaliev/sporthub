from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.http import HttpResponse

class Pole(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pole_detail', args=[str(self.id)])

class PoleImage(models.Model):
    image = models.ImageField(upload_to='media/')
    pole = models.ForeignKey(Pole, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.pole.title

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.image.url)

class Comment(models.Model):
    article = models.ForeignKey(
        Pole,
        on_delete=models.CASCADE,
        related_name = 'comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('pole_list')
