from django.db import models
from django.contrib.auth import settings
from django.utils import timezone


class PostFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="files/")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comments(models.Model):
    post = models.ForeignKey(PostFile, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approved(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment
