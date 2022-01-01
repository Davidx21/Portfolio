from django.contrib import admin

# Register your models here.
from .models import Skills,Project,Art,Contact, Company, Job

admin.site.register(Skills)
admin.site.register(Project)
admin.site.register(Art)
admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(Job)