from django.contrib import admin

# Register your models here.
from .models import Skills,Web,Illustration,Comic

admin.site.register(Skills)
admin.site.register(Web)
admin.site.register(Illustration)
admin.site.register(Comic)