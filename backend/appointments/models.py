from django.db import models

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    name = models.CharField(max_length=200, verbose_name="রোগীর নাম")
    phone = models.CharField(max_length=20, verbose_name="ফোন নম্বর")
    email = models.EmailField(blank=True, verbose_name="ইমেইল")
    age = models.PositiveIntegerField(verbose_name="বয়স")
    problem = models.TextField(verbose_name="সমস্যার বিবরণ")
    chamber = models.CharField(max_length=200, verbose_name="চেম্বার")
    preferred_date = models.DateField(verbose_name="পছন্দের তারিখ")
    preferred_time = models.CharField(max_length=50, verbose_name="পছন্দের সময়")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.preferred_date}"
