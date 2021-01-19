from django.contrib import admin
from faculty.models import DepartmentModel,CoursesModel,StudentModel,FacultyModel


admin.site.register(DepartmentModel)
admin.site.register(CoursesModel)
admin.site.register(StudentModel)
admin.site.register(FacultyModel)