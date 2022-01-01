from django.contrib import admin

# Register your models here.
from .models import Skills,Project,Art,Experience

admin.site.register(Skills)
admin.site.register(Project)
admin.site.register(Art)
admin.site.register(Experience)