from django.db import models
from multiselectfield import MultiSelectField


class Course(models.Model):
    COURSE_TYPE = (
        ('Theory', 'Theory'),
        ('Lab', 'Lab')
    )

    course_id = models.CharField(max_length=1000, primary_key=True)
    course_name = models.CharField(max_length=1000, null=True)
    course_type = models.CharField(max_length=200, null=True, choices=COURSE_TYPE)
    credit_hours = models.IntegerField(null=True)
    contact_hours = models.IntegerField(null=True)

    def __str__(self):
        return self.course_id + ' - ' + self.course_name






class Professor(models.Model):
    professor_id = models.CharField(max_length=2000,primary_key=True)
    professor_name = models.CharField(max_length=2000, null=True)
    working_hours = models.IntegerField(null=True)
    available_hours = models.IntegerField(null=True)
    def __str__(self):
        return self.professor_name




class Classroom(models.Model):
    CLASSRoom_TYPE = (
        ('Theory', 'Theory'),
        ('Lab', 'Lab')
    )
    classroom_id = models.CharField(max_length=2000, primary_key=True)
    classroom_name = models.CharField(max_length=2000, null=True)
    classroom_type = models.CharField(max_length=2000, null=True, choices=CLASSRoom_TYPE)
    def __str__(self):
        return self.classroom_id #+ ' - ' + self.classroom_name



class Class(models.Model):
    WEEK_DAY = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
    )

    class_id = models.CharField(max_length=2000, primary_key=True)
    class_name = models.CharField(max_length=2000, null=True)
    week_day = MultiSelectField(max_length=2000, choices=WEEK_DAY, max_choices=7)
    start_time = models.PositiveIntegerField(null=True)
    end_time = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.class_id #+ ' - ' + self.class_name


# table to store courses for class
class ClassCourse(models.Model):
    class Meta:
        unique_together = (('class_id', 'course_id'),)
    class_id = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,null=True, on_delete=models.CASCADE)



# to store classrooms for class
class SectionClassroom(models.Model):
    class Meta:
        unique_together = (('class_id', 'classroom_id'),)

    class_id = models.ForeignKey(Class,on_delete=models.CASCADE, default="")
    classroom_id = models.ForeignKey(Classroom,on_delete=models.CASCADE , default="")
    #def __str__(self):
     #   return self.class_id #+ ' - ' + self.classroom_id


class Activity(models.Model):
    ACTIVITY_TYPE = (
        ('Fixed', 'Fixed'),
        ('Replaceable', 'Replaceable')
    )
    activity_id = models.CharField(max_length=2000, primary_key=True)
    activity_type = models.CharField(max_length=2000, null=True, choices=ACTIVITY_TYPE)
    class_id = models.CharField(max_length=2000, null=True)
    classroom_id = models.CharField(max_length=2000, null=True)
    course_id = models.CharField(max_length=2000, null=True)
    professor_id = models.CharField(max_length=2000, null=True)
    day = models.CharField(max_length=2000, null=True)
    start_time = models.PositiveIntegerField(null=True)
    end_time = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.activity_id
