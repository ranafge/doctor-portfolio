from django.db import models

class News(models.Model):
    title_bn = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    summary_bn = models.TextField()
    summary_en = models.TextField()
    source = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title_en
