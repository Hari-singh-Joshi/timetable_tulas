from django.db import models
from django.contrib.auth.models import AbstractUser

DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]

SESSION_TYPE_CHOICES = [
    ('Tutorial', 'Tutorial'),
    ('Lecture', 'Lecture'),
    ('Lab', 'Lab'),
    ('Add_On', 'Add_On'),
    ('Minor_Project', 'Minor_Project'),
    ('internship', 'Internship'),
]

class Department(models.Model):
    DepartmentName = models.CharField(max_length=100, primary_key=True)
    HeadOfDepartment = models.CharField(max_length=100)
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.DepartmentName


class Teacher(AbstractUser):
   
    FirstName = models.CharField(max_length=100, null=True)
    MiddleName = models.CharField(max_length=100, blank=True, null=True)
    LastName = models.CharField(max_length=100, null=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName} ({self.username})"


class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    CourseCode = models.CharField(max_length=20, primary_key=True)
    CourseDescription = models.TextField(max_length=500, blank=True)
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.CourseName} ({self.CourseCode})"


class Venue(models.Model):
    VenueName = models.CharField(max_length=100, primary_key=True)
    IsCSEBlock = models.BooleanField(default=True)  
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.VenueName


SECTION_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('A1', 'A1'),
    ('B1', 'B1'),
    ('C1', 'C1'),
    ('D1', 'D1'),
    ('A2', 'A2'),
    ('B2', 'B2'),
    ('C2', 'C2'),
    ('D2', 'D2'),
    ('E', 'E'),
    ('F', 'F'),
    ('G', 'G'),
    ('H', 'H'),
]
START_TIME_CHOICES = [
    ('09:40', '9:40 AM'),
    ('10:30', '10:30 AM'),
    ('11:20', '11:20 AM'),
    ('11:30', '11:30 AM'),
    ('12:20', '12:20 PM'),
    ('13:10', '1:10 PM'),
    ('14:00', '2:00 PM'),
    ('14:50', '2:50 PM'),
    ('15:40', '3:40 PM'),
    ('16:30', '4:30 PM'),
]

END_TIME_CHOICES = [
    ('09:40', '9:40 AM'),
    ('10:30', '10:30 AM'),
    ('11:20', '11:20 AM'),
    ('11:30', '11:30 AM'),
    ('12:20', '12:20 PM'),
    ('13:10', '1:10 PM'),
    ('14:00', '2:00 PM'),
    ('14:50', '2:50 PM'),
    ('15:40', '3:40 PM'),
    ('16:30', '4:30 PM'),
]



from django.db.models import Q

from django.db import models

class TimeTable(models.Model):
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)
    Teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    Venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    Timestart = models.CharField(max_length=5, choices=START_TIME_CHOICES)
    TimeEnd = models.CharField(max_length=5, choices=END_TIME_CHOICES)
    Day = models.CharField(max_length=20, choices=DAY_CHOICES)
    Section = models.CharField(max_length=2, choices=SECTION_CHOICES, default=None)
    YearOfStudy = models.CharField(max_length=10) 
    Semester = models.CharField(max_length=10)  
    SessionType = models.CharField(max_length=20, choices=SESSION_TYPE_CHOICES)
    RegisteredDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Course} by {self.Teacher} in {self.Venue} on {self.Day} for {self.Section}"

    class Meta:
        ordering = ['Day', 'Timestart']
        constraints = [
    # Ensure a teacher is not scheduled for multiple classes at the same time on the same day
    models.UniqueConstraint(
        fields=['Teacher', 'Timestart', 'Day'],
        name='unique_teacher_timestart_day'
    ),
    # Ensure a venue is not double-booked at the same time on the same day
    models.UniqueConstraint(
        fields=['Venue', 'Timestart', 'Day'],
        name='unique_venue_timestart_day'
    ),
    # Ensure a section does not have multiple classes scheduled at the same time on the same day
    models.UniqueConstraint(
        fields=['Section', 'Timestart', 'Day'],
        name='unique_section_timestart_day'
    )
]
