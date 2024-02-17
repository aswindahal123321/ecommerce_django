from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    Heading = models.CharField(max_length=500, default="")
    cHeading = models.CharField(max_length=5000, default="")
    subHeading = models.CharField(max_length=500, default="")
    csubheading = models.CharField(max_length=5000, default="")
    category = models.CharField(max_length=50, default="")
    thumbnail = models.ImageField(upload_to='blog/images/', default="") 
    date_pub = models.DateField()
    author = models.CharField(max_length=50, default="")
    views = models.IntegerField(default=0)
    
    def __str__(self):
            return self.title
        

class BlogComment(models.Model):
    sno = models.AutoField(primary_key= True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Blog, on_delete = models.CASCADE)
    parent = models.ForeignKey('self', on_delete = models.CASCADE, null=True)
    timestamp = models.DateField(default=now)
        
