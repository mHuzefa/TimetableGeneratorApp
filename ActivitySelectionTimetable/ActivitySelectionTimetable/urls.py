
from django.contrib import admin
from django.urls import path, include
import ActivitySelectionTimetable.settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('timetableapp.urls')),


]
