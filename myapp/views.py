
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import UserProfile
from .models import Course
from .forms import CourseForm
from .models import StudentRecord
from .models import Enrollment
from .forms import StudentRecordForm
from .forms import EnrollmentForm
from .models import Attendance
from .models import Grade
from .forms import AttendanceForm
from .forms import GradeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser
def is_faculty(user):

    if user.is_superuser:
        return True

    return (
        hasattr(user, 'userprofile')
        and user.userprofile.role == 'Faculty'
    )


def is_student(user):

    return (
        hasattr(user, 'userprofile')
        and user.userprofile.role == 'Student'
    )


def home(request):

    return render(
        request,
        'home.html'
    )


def register(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            role = form.cleaned_data['role']

            UserProfile.objects.create(
                user=user,
                role=role
            )

            group, created = Group.objects.get_or_create(
                name=role
            )

            user.groups.add(group)

            return redirect(
                'login'
            )

    return render(
        request,
        'register.html',
        {'form': form}
    )


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )

        else:

            messages.error(
                request,
                'Invalid Username or Password'
            )

    return render(
        request,
        'login.html'
    )


def user_logout(request):

    logout(request)

    return redirect(
        'home'
    )


@login_required
def dashboard(request):

    if request.user.is_superuser:

        return redirect(
            'admin_dashboard'
        )

    role = request.user.userprofile.role

    if role == 'Faculty':

        return redirect(
            'faculty_dashboard'
        )

    elif role == 'Student':

        return redirect(
            'student_dashboard'
        )

    return redirect(
        'home'
    )
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):

    total_students = UserProfile.objects.filter(
        role='Student'
    ).count()

    total_faculty = UserProfile.objects.filter(
        role='Faculty'
    ).count()

    total_courses = Course.objects.count()

    total_enrollments = Enrollment.objects.count()

    context = {

        'students': total_students,

        'faculty': total_faculty,

        'courses': total_courses,

        'enrollments': total_enrollments

    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )
@login_required
@user_passes_test(is_faculty)
def faculty_dashboard(request):

    return render(
        request,
        'faculty_dashboard.html'
    )


@login_required
@user_passes_test(is_student)
def student_dashboard(request):

    return render(
        request,
        'student_dashboard.html'
    )
@login_required

def course_list(request):

    courses = Course.objects.all()

    return render(
        request,
        'course_list.html',
        {'courses': courses}
    )
@login_required
@user_passes_test(is_faculty)
def add_course(request):

    form = CourseForm()

    if request.method == "POST":

        form = CourseForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'course_list'
            )

    return render(
        request,
        'course_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_faculty)
def edit_course(request,id):

    course = Course.objects.get(
        id=id
    )

    form = CourseForm(
        instance=course
    )

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            instance=course
        )

        if form.is_valid():

            form.save()

            return redirect(
                'course_list'
            )

    return render(
        request,
        'course_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_faculty)
def delete_course(request,id):

    course = Course.objects.get(
        id=id
    )

    course.delete()

    return redirect(
        'course_list'
    )
@login_required
@user_passes_test(is_admin)
def student_list(request):

    students = StudentRecord.objects.all()

    return render(
        request,
        'student_list.html',
        {'students': students}
    )
@login_required
@user_passes_test(is_admin)
def add_student(request):

    form = StudentRecordForm()

    if request.method == 'POST':

        form = StudentRecordForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'student_list'
            )

    return render(
        request,
        'student_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_admin)
def edit_student(request,id):

    student = StudentRecord.objects.get(
        id=id
    )

    form = StudentRecordForm(
        instance=student
    )

    if request.method == 'POST':

        form = StudentRecordForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect(
                'student_list'
            )

    return render(
        request,
        'student_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_admin)
def delete_student(request,id):

    student = StudentRecord.objects.get(
        id=id
    )

    student.delete()

    return redirect(
        'student_list'
    )
@login_required
@user_passes_test(is_faculty)
def enrollment_list(request):

    enrollments = Enrollment.objects.all()

    return render(
        request,
        'enrollment_list.html',
        {'enrollments': enrollments}
    )
@login_required
@user_passes_test(is_faculty)
def add_enrollment(request):

    form = EnrollmentForm()

    if request.method == 'POST':

        form = EnrollmentForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'enrollment_list'
            )

    return render(
        request,
        'enrollment_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_faculty)
def delete_enrollment(request,id):

    enrollment = Enrollment.objects.get(
        id=id
    )

    enrollment.delete()

    return redirect(
        'enrollment_list'
    )
@login_required
@user_passes_test(is_faculty)
def attendance_list(request):

    attendance = Attendance.objects.all()

    return render(
        request,
        'attendance_list.html',
        {'attendance': attendance}
    )
@login_required
@user_passes_test(is_faculty)
def add_attendance(request):

    form = AttendanceForm()

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'attendance_list'
            )

    return render(
        request,
        'attendance_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_faculty)
def delete_attendance(request,id):

    attendance = Attendance.objects.get(
        id=id
    )

    attendance.delete()

    return redirect(
        'attendance_list'
    )
@login_required
@user_passes_test(is_faculty)
def grade_list(request):

    grades = Grade.objects.all()

    return render(
        request,
        'grade_list.html',
        {'grades': grades}
    )
@login_required
@user_passes_test(is_faculty)
def add_grade(request):

    form = GradeForm()

    if request.method == 'POST':

        form = GradeForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'grade_list'
            )

    return render(
        request,
        'grade_form.html',
        {'form': form}
    )
@login_required
@user_passes_test(is_faculty)
def delete_grade(request,id):

    grade = Grade.objects.get(
        id=id
    )

    grade.delete()

    return redirect(
        'grade_list'
    )
@login_required
def my_attendance(request):

    attendance = Attendance.objects.filter(
        student=request.user
    )

    return render(
        request,
        'my_attendance.html',
        {'attendance': attendance}
    )
@login_required
def my_grades(request):

    grades = Grade.objects.filter(
        student=request.user
    )

    return render(
        request,
        'my_grades.html',
        {'grades': grades}
    )
def is_admin(user):

    return user.is_superuser


@login_required
def enroll_course(request, course_id):

    course = Course.objects.get(id=course_id)

    already_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    if not already_enrolled:

        Enrollment.objects.create(
            student=request.user,
            course=course
        )

    return redirect('my_enrollments')
@login_required
def my_enrollments(request):

    enrollments = Enrollment.objects.filter(
        student=request.user
    )

    return render(
        request,
        'my_enrollments.html',
        {'enrollments': enrollments}
    )