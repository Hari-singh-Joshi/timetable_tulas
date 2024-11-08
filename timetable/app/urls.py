from . import views
from django.urls import path

urlpatterns = [
    
    path("", views.timetable_view, name='timetable'),
 
    
   
       
]
