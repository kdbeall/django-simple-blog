from django.db import models

# Create your models here.


class Entry(models.Model):
    class Meta:
        verbose_name_plural = "entries"
