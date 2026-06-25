from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course
from .models import StudentRecord
from .models import Enrollment
from .models import Attendance
from .models import Grade


class RegisterForm(UserCreationForm):

    ROLE_CHOICES = [
        ('Faculty', 'Faculty'),
        ('Student', 'Student'),
    ]

    email = forms.EmailField()

    role = forms.ChoiceField(
        choices=ROLE_CHOICES
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2'
        ]


class CourseForm(forms.ModelForm):

    class Meta:

        model = Course

        fields = [
            'course_name',
            'course_code',
            'description',
            'faculty'
        ]



class StudentRecordForm(forms.ModelForm):

    class Meta:

        model = StudentRecord

        fields = [
            'student',
            'department',
            'semester',
            'phone'
        ]


class EnrollmentForm(forms.ModelForm):

    class Meta:

        model = Enrollment

        fields = [
            'student',
            'course'
        ]



class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = [
            'student',
            'course',
            'date',
            'status'
        ]


class GradeForm(forms.ModelForm):

    class Meta:

        model = Grade

        fields = [
            'student',
            'course',
            'marks',
            'grade'
        ]