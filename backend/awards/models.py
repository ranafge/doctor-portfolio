from django.db import models

class Award(models.Model):
    icon = models.CharField(max_length=100, default="fas fa-trophy")
    title_bn = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    organization_bn = models.CharField(max_length=200)
    organization_en = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title_en
