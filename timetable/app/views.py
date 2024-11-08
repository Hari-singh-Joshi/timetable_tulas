from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import TimeTable

def timetable_view(request):
    # Get the current date
    today = timezone.now().date()
    seven_days_later = today + timedelta(days=7)
    
    # Retrieve filter parameters
    year = request.POST.get('year', None)
    semester = request.POST.get('semester', None)
    venue = request.POST.get('venue', None)
    section = request.POST.get('Section', None)
    day = request.POST.get('Day', None)

    # Only build the query if year and semester are provided
    if year and semester and section:
        # Base queryset for filtering
        timetable = TimeTable.objects.filter(YearOfStudy=year, Semester=semester)

        # Additional filters
        if venue:
            timetable = timetable.filter(Venue__VenueName=venue)
        
        if section:
            timetable = timetable.filter(Section__startswith=section)

        # Days of the week in desired order
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Filter based on the specific day if provided
        if day:
            # Only filter for the specific day selected
            timetable = timetable.filter(Day=day)
        else:
            # Otherwise, filter for the entire week, starting from today
            timetable = timetable.filter(
                Day__in=[(today + timedelta(days=i)).strftime('%A') for i in range(7)]
            )

        # Sort the results by day and start time
        timetable = sorted(timetable, key=lambda x: (day_order.index(x.Day), x.Timestart))

    else:
        timetable = None  # No results if year, semester, or section aren't provided

    # Context for template
    context = {
        'timetable': timetable,
        'year': year,
        'semester': semester,
        'venue': venue,
        'section': section,
        'today': today,
        'seven_days_later': seven_days_later,
        'day': day,
    }
    
    return render(request, 'timetable.html', context)
