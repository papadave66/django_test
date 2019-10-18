from django.contrib import admin
from .models import student,course,study,courseType,teach,teacher

admin.site.register(student)
admin.site.register(course)
admin.site.register(study)
admin.site.register(courseType)
admin.site.register(teach)
admin.site.register(teacher)
