from django.db import models

# Create your models here.
class blog_post(models.Model):
    title=models.TextField()
    isi=models.TextField(null=True)
    thumbnail=models.ImageField(upload_to='images/')
    tanggal=models.DateField(auto_now_add=True)
    kategori=(('article','article'),('music','music'))
    category = models.CharField(max_length=10, choices=kategori,null=True)
    download=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title

class home(models.Model):
    welcome=models.TextField()
    webname=models.CharField(max_length=50,null=True)
    text=models.TextField(null=True)
    cover=models.ImageField(upload_to='images/')
    github_link=models.TextField(null=True)
    twitter_link=models.TextField(null=True)
    logo=models.ImageField(blank=True,null=True)
    def __str__(self):
        return "Modify Home"

class about_me(models.Model):
    profile=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return 'modify about me'

    