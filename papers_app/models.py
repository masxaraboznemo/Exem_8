from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.fullname
    
    
    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField( null=True, blank=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE )
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'papers'
        verbose_name = 'Paper'
        verbose_name_plural = 'Papers'
        