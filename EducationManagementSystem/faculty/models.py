from django.db import models

class DepartmentModel(models.Model):
    number = models.AutoField(primary_key=True),
    name = models.CharField(max_length=200,unique=True)

class CoursesModel(models.Model):
    number = models.AutoField(primary_key=True),
    name = models.CharField(max_length=200, unique=True)
    course_department = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)

class FacultyModel(models.Model):
    number = models.AutoField(primary_key=True),
    name = models.CharField(max_length=200)
    contactno = models.IntegerField(unique=True)
    faculty_courses = models.ForeignKey(CoursesModel,on_delete=models.CASCADE)

class StudentModel(models.Model):
    number = models.AutoField(primary_key=True),
    name = models.CharField(max_length=200)
    contactno = models.IntegerField(unique=True)
    email = models.CharField(max_length=200,unique=True)
    student_department  = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)