from django.db import models

class student(models.Model):
    student_id = models.CharField(max_length=10,primary_key=True)
    student_name = models.CharField(null=False,max_length=10)
    student_course = models.ManyToMany(course,on_delete=models.CASCADE) # TODO:1:N? OR N:M???

class course(models.Model):
    course_name = models.CharField(null=False,max_length=10)
    teacher_name = models.ForeignKey(teacher, on_delete=models.CASCADE)

class course_type(models.Model):
    course_type_name = models.CharField(null=False,max_length=10)


class teacher(models.Model):
    teacher_name = models.CharField(null=False,max_length=10)
    teacher_id = models.AutoField(primary_key=True)
    
