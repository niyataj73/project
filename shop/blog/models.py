from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    STATUSE_CHOICES= (
        ('D' , 'Draft'),
        ('p' , 'Publish')
    )
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,max_length=100)
    desc=models.TextField()
    image=models.ImageField(upload_to="image")
    publish=models.DateTimeField(default=timezone.now)
    Create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUSE_CHOICES)
    
    def __str__(self):
        return self.title
