from django.db import models

class Publication(models.Model):
    number = models.PositiveIntegerField(default=1)
    title = models.TextField()
    journal = models.CharField(max_length=300)
    year = models.PositiveIntegerField()
    tag = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title[:60]
