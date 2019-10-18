from django.shortcuts import render
from .models import student,course,study,courseType,teach,teacher

def index(request):
    student_list = student.objects.all()
    course_list = course.objects.all()
    teacher_list = teacher.objects.all()
    teach_list = teach.objects.all()
    study_list = study.objects.all()
    return render(request, 'index.html', context={'student_list':student_list,'course_list':course_list,'teacher_list':teacher_list})
