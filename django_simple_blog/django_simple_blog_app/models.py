from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"
