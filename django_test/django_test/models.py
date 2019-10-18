from django.db import models

class student(models.Model):
    SEX = (
        ('male','male'),
        ('female','female')
    )
    student_id = models.CharField(max_length=10,primary_key=True)
    student_name = models.CharField(null=False,max_length=10)
    student_sex = models.CharField(choices=SEX,max_length=10)
    student_birth = models.DateTimeField()
    student_address = models.CharField(max_length=50)

class course(models.Model):
    course_id = models.CharField(max_length=10,primary_key=True)
    course_name = models.CharField(null=False,max_length=10)
    course_time = models.IntegerField()
    course_score = models.IntegerField()
    course_book = models.CharField(max_length=50)
    course_type_info = models.ForeignKey('courseType', on_delete=models.CASCADE)

class study(models.Model):
    student_id = models.ForeignKey('student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    score = models.IntegerField()

class courseType(models.Model):
    course_type_id = models.CharField(max_length=10,primary_key=True)
    course_type_name = models.CharField(null=False,max_length=10)

class teach(models.Model):
    teacher_id = models.ForeignKey('teacher', on_delete=models.CASCADE)
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

class teacher(models.Model):
    SEX = (
        ('male','male'),
        ('female','female')
    )
    teacher_name = models.CharField(null=False,max_length=10)
    teacher_id = models.AutoField(primary_key=True)
    teacher_sex = models.CharField(choices=SEX, max_length=10)
    teacher_birth = models.DateTimeField()
    teacher_title = models.CharField(max_length=10)
    teacher_academic = models.CharField(max_length=10)
    teacher_work = models.DateTimeField()
