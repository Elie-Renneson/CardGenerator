from django.db import models

class Phrase(models.Model):
    texte = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, default="Pinterest.png")

    def __str__(self):
        return f"{self.texte}"
