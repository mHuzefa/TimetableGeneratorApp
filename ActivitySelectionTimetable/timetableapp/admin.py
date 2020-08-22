from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Classroom)
admin.site.register(Class)
admin.site.register(ClassCourse)
admin.site.register(SectionClassroom)
admin.site.register(Activity)

