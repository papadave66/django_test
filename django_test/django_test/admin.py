from django.contrib import admin
from .models import student,course,course_type,teacher

class showStudent(admin.ModelAdmin):
    list = ['student_name','student_course']

admin.site.register(student)
admin.site.register(student)
admin.site.register(course)
