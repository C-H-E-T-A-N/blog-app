from django.db import models

# Create your models here.
class BlogObj(models.Model):
    sr_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200, default="")
    content = models.TextField()
    slug = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
     