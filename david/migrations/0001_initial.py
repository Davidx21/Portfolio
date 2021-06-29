# Generated by Django 3.1.4 on 2021-06-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='static/images')),
                ('image1', models.ImageField(upload_to='static/images')),
                ('image2', models.ImageField(upload_to='static/images')),
                ('image3', models.ImageField(upload_to='static/images')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Illustration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='static/images')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('presentation', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='static/images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
                ('github', models.CharField(blank=True, max_length=300, null=True)),
                ('date', models.DateField()),
                ('skills', models.ManyToManyField(to='david.Skills')),
            ],
        ),
    ]
