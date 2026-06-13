from django.db import models

class Chamber(models.Model):
    name_bn = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    subtitle_bn = models.CharField(max_length=200)
    subtitle_en = models.CharField(max_length=200)
    address_bn = models.TextField()
    address_en = models.TextField()
    time_bn = models.CharField(max_length=100)
    time_en = models.CharField(max_length=100)
    days_bn = models.CharField(max_length=100)
    days_en = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    map_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name_en
