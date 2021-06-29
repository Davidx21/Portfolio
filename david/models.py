from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="static/images",blank=True, null=True)
    nivel = models.IntegerField(default=50)
    date = models.DateField()

    def __str__(self):
        return (str(self.name))
    
    class Meta:
        verbose_name_plural = "Skills"

class Web(models.Model):
    name = models.CharField(max_length = 300)
    presentation = models.CharField(max_length = 500)
    skills = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to="static/images")
    image2 = models.ImageField(upload_to="static/images",blank=True, null=True)
    image3 = models.ImageField(upload_to="static/images",blank=True, null=True)
    image4 = models.ImageField(upload_to="static/images",blank=True, null=True)
    link = models.CharField(max_length = 300,blank=True, null=True)
    github = models.CharField(max_length = 300,blank=True, null=True)
    date = models.DateField()
    def __str__(self):
        return (str(self.name))
    
    class Meta:
        verbose_name_plural = "Web Projects"

class Illustration(models.Model):
    name =  models.CharField(max_length = 300)
    image = models.ImageField(upload_to="static/images")
    date = models.DateField()
    def __str__(self):
        return (str(self.name))

class Comic(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to="static/images")
    image1 = models.ImageField(upload_to="static/images")
    image2 = models.ImageField(upload_to="static/images")
    image3 = models.ImageField(upload_to="static/images")
    date = models.DateField()
    def __str__(self):
        return (str(self.name))