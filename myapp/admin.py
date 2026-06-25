from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(StudentRecord)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Grade)
