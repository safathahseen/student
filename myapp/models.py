from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = (
         ('Admin', 'Admin'),
         ('Faculty', 'Faculty'),
        ('Student', 'Student'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.user.username


class Course(models.Model):

    course_name = models.CharField(
        max_length=100
    )

    course_code = models.CharField(
        max_length=20,
        unique=True
    )

    description = models.TextField()

    faculty = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.course_name


class StudentRecord(models.Model):

    student = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    department = models.CharField(
        max_length=100
    )

    semester = models.IntegerField()

    phone = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.student.username


class Enrollment(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrolled_on = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.course.course_name}"


class Attendance(models.Model):

    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.student.username} - {self.status}"


class Grade(models.Model):

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    marks = models.IntegerField()

    grade = models.CharField(
        max_length=5
    )

    def __str__(self):
        return f"{self.student.username} - {self.grade}"


# Create your models here.
