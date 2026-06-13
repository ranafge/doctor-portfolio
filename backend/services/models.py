from django.db import models

class Service(models.Model):
    icon = models.CharField(max_length=100, default="fas fa-stethoscope")
    title_bn = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    description_bn = models.TextField()
    description_en = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title_en
