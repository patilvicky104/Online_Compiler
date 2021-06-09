from django.db import models


class Savedata(models.Model):
    name = models.CharField(max_length=255)
    codedata = models.TextField()
    outputarea = models.TextField(null=True)

    def __str__(self):
        return self.name
