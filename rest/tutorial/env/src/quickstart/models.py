from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'uploads/', default = 'uploads/no-img.jpg')
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
