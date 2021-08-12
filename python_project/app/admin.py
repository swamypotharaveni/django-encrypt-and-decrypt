from django.contrib import admin
from app.models import Student
class studeadmin(admin.ModelAdmin):
    list_display=['contact','course','date']
admin.site.register(Student,studeadmin)
# Register your models here.
