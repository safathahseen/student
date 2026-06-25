from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),
    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
    ),

    path(
        'faculty-dashboard/',
        views.faculty_dashboard,
        name='faculty_dashboard'
    ),

    path(
        'student-dashboard/',
        views.student_dashboard,
        name='student_dashboard'
    ),
    path(
    'courses/',
    views.course_list,
    name='course_list'
),

path(
    'courses/add/',
    views.add_course,
    name='add_course'
),

path(
    'courses/edit/<int:id>/',
    views.edit_course,
    name='edit_course'
),

path(
    'courses/delete/<int:id>/',
    views.delete_course,
    name='delete_course'
),
# Student Records

path(
    'students/',
    views.student_list,
    name='student_list'
),

path(
    'students/add/',
    views.add_student,
    name='add_student'
),

path(
    'students/edit/<int:id>/',
    views.edit_student,
    name='edit_student'
),

path(
    'students/delete/<int:id>/',
    views.delete_student,
    name='delete_student'
),

# Enrollment

path(
    'enrollments/',
    views.enrollment_list,
    name='enrollment_list'
),

path(
    'enrollments/add/',
    views.add_enrollment,
    name='add_enrollment'
),

path(
    'enrollments/delete/<int:id>/',
    views.delete_enrollment,
    name='delete_enrollment'
),
# Attendance

path(
    'attendance/',
    views.attendance_list,
    name='attendance_list'
),

path(
    'attendance/add/',
    views.add_attendance,
    name='add_attendance'
),

path(
    'attendance/delete/<int:id>/',
    views.delete_attendance,
    name='delete_attendance'
),

# Grades

path(
    'grades/',
    views.grade_list,
    name='grade_list'
),

path(
    'grades/add/',
    views.add_grade,
    name='add_grade'
),

path(
    'grades/delete/<int:id>/',
    views.delete_grade,
    name='delete_grade'
),

# Student Records

path(
    'my-attendance/',
    views.my_attendance,
    name='my_attendance'
),

path(
    'my-grades/',
    views.my_grades,
    name='my_grades'
),
path(
    'enroll/<int:course_id>/',
    views.enroll_course,
    name='enroll_course'
),

path(
    'my-enrollments/',
    views.my_enrollments,
    name='my_enrollments'
),

]