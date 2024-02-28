from django.db import models


class Careers(models.Model):
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title