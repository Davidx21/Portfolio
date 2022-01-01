from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
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

class Company(models.Model):
    name = models.CharField(max_length = 300)
    DateField = models.DateField(auto_now=True)
    def __str__(self):
        return (str(self.name))
    class Meta:
        verbose_name_plural = "Companies"

class Job(models.Model):
    name = models.CharField(max_length = 300)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=CASCADE)
    def __str__(self):
        return (str(self.name))
    class Meta:
        verbose_name_plural = "Jobs"

class Project(models.Model):
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
        verbose_name_plural = "Projects"

class Art(models.Model):
    name =  models.CharField(max_length = 300)
    image = models.ImageField(upload_to="static/images")
    date = models.DateField()
    def __str__(self):
        return (str(self.name))

class Contact(models.Model):
    dateTime = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 300)
    subject = models.CharField(max_length = 300)
    message = models.TextField()
    def __str__(self):
        return (str(self.name) +"_" + str(self.subject) + "_" + str(self.dateTime))