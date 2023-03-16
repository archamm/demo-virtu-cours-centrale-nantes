from django.db import models

class Tweet(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.author}: {self.text}"
