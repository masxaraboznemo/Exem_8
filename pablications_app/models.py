from django.db import models

# Create your models here.
class Pablication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'pablications'
        verbose_name = 'Pablication'
        verbose_name_plural = 'Pablications'
        