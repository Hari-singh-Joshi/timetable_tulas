from django.contrib import admin
from .models import Department, Teacher, Course, Venue, TimeTable


# Customize the display for the Department model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentName', 'HeadOfDepartment', 'RegisteredDate')
    search_fields = ('DepartmentName', 'HeadOfDepartment')
    list_filter = ('RegisteredDate',)
    readonly_fields = ('RegisteredDate',)


# Customize the display for the Teacher model
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'FirstName', 'LastName', 'Department', 'RegisteredDate')
    search_fields = ('FirstName', 'LastName', 'username', 'Department__DepartmentName')
    list_filter = ('Department', 'RegisteredDate')
    readonly_fields = ('RegisteredDate',)

    # When editing teachers, display only specific fields
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'FirstName', 'MiddleName', 'LastName', 'Department', 'is_active', 'is_staff')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined', 'RegisteredDate'),
        }),
    )


# Customize the display for the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseName', 'CourseCode', 'RegisteredDate')
    search_fields = ('CourseName', 'CourseCode')
    list_filter = ('RegisteredDate',)
    readonly_fields = ('RegisteredDate',)


# Customize the display for the Venue model
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('VenueName', 'IsCSEBlock', 'RegisteredDate')
    search_fields = ('VenueName',)
    list_filter = ('IsCSEBlock', 'RegisteredDate')
    readonly_fields = ('RegisteredDate',)


# Customize the display for the TimeTable model
@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('Course', 'Teacher', 'Venue', 'Day','Section','Timestart', 'TimeEnd', 'YearOfStudy', 'Semester', 'SessionType')
    search_fields = ('Course__CourseName', 'Teacher__FirstName', 'Teacher__LastName', 'Venue__VenueName', 'Day', 'Section','YearOfStudy', 'Semester')
    list_filter = ('Day', 'YearOfStudy', 'Semester', 'SessionType', 'Venue', 'Teacher','Section')
    readonly_fields = ('RegisteredDate',)
    ordering = ['Day', 'Timestart']

    # Allow inline editing of timetable records in admin
    fieldsets = (
        (None, {
            'fields': ('Course', 'Teacher', 'Venue', 'Day','Section', 'Timestart', 'TimeEnd', 'YearOfStudy', 'Semester', 'SessionType')
        }),
        ('Important dates', {
            'fields': ('RegisteredDate',)
        }),
    )
