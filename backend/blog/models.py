from django.db import models
from cloudinary.models import CloudinaryField  

class BlogPost(models.Model):
    title_bn = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)
    summary_bn = models.TextField()
    summary_en = models.TextField()
    content_bn = models.TextField(blank=True)
    content_en = models.TextField(blank=True)
    category_bn = models.CharField(max_length=100)
    category_en = models.CharField(max_length=100)
    image = CloudinaryField('image', blank=True, null=True)
    date = models.DateField()
    read_time = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return self.title_en