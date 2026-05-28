from django.db import models
from datetime import timezone
from django.utils.text import slugify

# Create your models here.
class Tenant(models.Model):

    CATEGORY_CHOICES = [
        ('fintech', 'Fintech'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    
    