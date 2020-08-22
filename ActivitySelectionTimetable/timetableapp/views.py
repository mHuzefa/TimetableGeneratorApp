
import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

from .models import Course


def loginPage(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('selection')
    else:
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password= password )
            if user is not None:
                login(request, user)
                return redirect('selection')
            else:
                messages.info(request, 'Username or Password is Incorrect')
                return render(request, 'timetableapp/login.html', context)

        
        return render(request, 'timetableapp/login.html', context)


def Logout(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('selection')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created successfully for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'timetableapp/register.html', context)

def home(request):
    course = CourseForm()
    professor = ProfessorForm()
    classroom = ClassroomForm()
    section = ClassForm()
    sectioncourse = ClassCourseForm()
    sectionclassroom = SectionClassroomForm()
    activity = ActivityForm()
    context = {

                'course': course,'professor': professor,
                'classroom': classroom, 'section': section,
                'sectioncourse': sectioncourse, 'sectionclassroom': sectionclassroom, 'activity': activity

            }


    return render(request, 'timetableapp/home.html', context)


@login_required(login_url='login')
def CourseView(request):
    course = CourseForm()
    context = {'course': course}

    if request.method == 'POST':
        course = CourseForm(request.POST)
        if course.is_valid():
            messages.success(request, 'Course has been added successfully.')
            course.save()
        else:
            messages.success(request, 'Course already exists or you have added wrong attributes.')


    return render(request, 'timetableapp/AddCourse.html', context)
@login_required(login_url='login')
def CourseTable(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'timetableapp/CourseTable.html', context)
@login_required(login_url='login')
def updateCourseView(request, pk):
    form = Course.objects.get(course_id=pk)
    course = CourseForm(instance=form)
    context = {'course': course}
    if request.method == 'POST':
        course = CourseForm(request.POST, instance=form)
        if course.is_valid():
            course.save()
            return redirect('/course_view')
    return render(request, 'timetableapp/AddCourse.html', context)

@login_required(login_url='login')
def deleteCourse(request, pk):
    delete_course = Course.objects.get(course_id=pk)
    context = {'course_delete': delete_course}
    if request.method == 'POST':
        delete_course.delete()
        return redirect('/course_view')

    return render(request, 'timetableapp/delete.html', context)

@login_required(login_url='login')
def ProfessorView(request):
    professor = ProfessorForm()
    professor1 = Professor.objects.all()

    context = {'professor': professor, 'professor1': professor1}
    if request.method == 'POST':
        professor = ProfessorForm(request.POST)
        if professor.is_valid():
            messages.success(request, 'Professor has been added successfully.')
            professor.save()
        else:
            messages.success(request, 'Professor already exists or you have added wrong attributes.')
    return render(request, 'timetableapp/AddProfessor.html', context)
@login_required(login_url='login')
def ProfessorTable(request):
    professor1 = Professor.objects.all()
    context = {'professor1': professor1}
    return render(request, 'timetableapp/ProfessorTable.html', context)
@login_required(login_url='login')
def updateProfessorView(request, pk):
    professor = Professor.objects.get(professor_id=pk)
    form = ProfessorForm(instance=professor)
    context = {'form': form}
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('/add-professor')
    return render(request, 'timetableapp/ViewSection.html', context)

@login_required(login_url='login')
def deleteProfessor(request, pk):
    deleteprofessor = Professor.objects.get(professor_id=pk)
    context = {'delete': deleteprofessor}
    if request.method == 'POST':
        deleteprofessor.delete()
        return redirect('/professor_view')

    return render(request, 'timetableapp/deleteProfessor.html', context)



@login_required(login_url='login')
def ClassroomView(request):
    classroom = ClassroomForm()
    classes = Classroom.objects.all()
    context = {'classroom': classroom, 'classes': classes}
    if request.method == 'POST':
        classroom = ClassroomForm(request.POST)
        if classroom.is_valid():
            messages.success(request, 'Classroom has been added.')
            classroom.save()
        else:
            messages.error(request, 'Do not enter the same class ID')
    return render(request, 'timetableapp/AddClassroom.html', context)
@login_required(login_url='login')
def ClassroomTable(request):
    classrooms = Classroom.objects.all()
    context = {'classrooms': classrooms}
    return render(request, 'timetableapp/ClassroomTable.html', context)
@login_required(login_url='login')
def updateClassroomView(request, pk):
    classroom = Classroom.objects.get(classroom_id=pk)
    form = ClassroomForm(instance=classroom)
    context = {'form': form}
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('/classroom_view')
    return render(request, 'timetableapp/ViewSection.html', context)
@login_required(login_url='login')
def deleteClassroom(request, pk):
    deleteClassroom = Classroom.objects.get(classroom_id=pk)
    context = {'delete': deleteClassroom}
    if request.method == 'POST':
        deleteClassroom.delete()
        return redirect('/classroom_view')

    return render(request, 'timetableapp/deleteClassroom.html', context)



@login_required(login_url='login')
def ClassView(request):
    section = ClassForm()
    sections = Class.objects.all()
    context = {'section': section, 'sections': sections}
    if request.method == 'POST':
        section = ClassForm(request.POST)
        if section.is_valid():  
            messages.success(request, 'Class has been added.')
            section.save()
            return redirect('/add-classcourse')    # add 
        else:
            messages.error(request, 'Do not enter the same class ID')
    return render(request, 'timetableapp/AddClass.html', context)
@login_required(login_url='login')
def ClassCourseView(request):
    sectioncourse = ClassCourseForm()
    sectioncourses = ClassCourse.objects.all()
    #section = Class.objects.get(class_id=id)
    context = {'sectioncourse': sectioncourse, 'sectioncourses': sectioncourses}
    if request.method == 'POST':
        sectioncourse = ClassCourseForm(request.POST)
        if sectioncourse.is_valid():
            messages.success(request, "Course added for class.")
            sectioncourse.save()
        else:
            messages.error(request, 'Can not add duplicate course for class.')
    return render(request, 'timetableapp/AddClassCourse.html', context)

@login_required(login_url='login')
def SectionRoomView(request):
    sectionroom = SectionClassroomForm()
    sectionrooms = SectionClassroom.objects.all()
    context = {'sectionroom': sectionroom, 'sectionrooms': sectionrooms}
    if request.method == 'POST':
        sectionroom == SectionClassroomForm(request.POST)
        if sectionroom.is_valid():
            messages.success(request, "Room added for the class")
            sectionroom.save()
        else:
            messages.error(request, 'Can not add duplicate rooms for a class')
    return render(request, 'timetableapp/AddSectionClassrooms.html', context)

@login_required(login_url='login')
def updateClassView(request, pk):
    section = Class.objects.get(class_id=pk)
    form = ClassForm(instance=section)
    context = {'form': form}
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('/add-classcourse')
    return render(request, 'timetableapp/ViewClass.html', context)


@login_required(login_url='login')
def deleteClass(request, pk):
    deleteClass = Class.objects.get(class_id=pk)
    context = {'delete': deleteClass}
    if request.method == 'POST':
        deleteActivities(pk)
        deleteCLassCourses(pk)
        deleteSectionClassrooms(pk)
        deleteClass.delete()

        return redirect('/class-view')

    return render(request, 'timetableapp/deleteClass.html', context)


def deleteCLassCourses(id):
    ClassCourse.objects.filter(class_id=id).delete()

def deleteSectionClassrooms(id):
    SectionClassroom.objects.filter(class_id=id).delete()




@login_required(login_url='login')
def ClassTable(request):
    sections = Class.objects.all()
    context = {'sections': sections}
    return render(request, 'timetableapp/ClassTable.html', context)




def WeekDayFormView(request):
    weekdayform = WeekDaysForm()
    context = {'form':weekdayform}
    if request.method == 'POST':
        weekdayform = WeekDaysForm(request.POST)
        if weekdayform.is_valid():
            weekdayform.save()
            messages.success(request, 'Class has been added.')
        else:
            messages.error(request, 'Do not enter the same class ID')
    return render(request, 'timetableapp/weekdays.html', context)



class Room:
    def __init__(self):
        self.ID = None
        self.TYPE = None

    #def __init__(self, id, type):
     #   self.ID = id
      #  self.TYPE = type




def AddSchedule(request):
    schedule = ScheduleForm()
    schedules = WeekSchedule.objects.all()
    context = {'schedule': schedule, 'schedules': schedules}
    if request.method == 'POST':
        schedule = ScheduleForm(request.POST)
        if schedule.is_valid():
            messages.success(request, "Schedule Added.")
            schedule.save()
        else:
            messages.error(request, 'Do not enter the same class ID')
    return render(request, 'timetableapp/AddClass.html', context)


@login_required(login_url='login')
def TimeTable(request):
    sections = Class.objects.all()
    context = {'sections': sections}
    return render(request, 'timetableapp/TimeTable.html', context)



@login_required(login_url='login')
def GenerateTimeTable(request, id):
    try:
        section = Class.objects.get(class_id=id)
        sectioncourses = list(ClassCourse.objects.filter(class_id=id))
        sectionrooms = list(SectionClassroom.objects.filter(class_id=id))
        if len(sectioncourses) > 0:
            if len(sectionrooms) > 0:
                if Activity.objects.filter(class_id=id).count() != 0:
                    #Activity.objects.filter(class_id=section.class_id).delete()
                    deleteActivities(id)
                totalDays = len(section.week_day)
                totalRooms = len(sectionrooms)
                workingHours = totalDays * (section.end_time - section.start_time)
                # getting class room data
                class_rooms = [Room() for i in range(totalRooms)]
                for i in range(len(sectionrooms)):
                    room = Classroom.objects.get(classroom_id=sectionrooms[i].classroom_id)
                    class_rooms[i].ID = room.classroom_id
                    class_rooms[i].TYPE = room.classroom_type
                    # variable to save index of class room being used
                roomNum = random.randint(0, totalRooms - 1)
                lecDay = 0
                lecStartTime = 0
                DupNum = 0
                for k in range(0, len(sectioncourses)):
                    if DupNum > (workingHours + 5):
                        break
                    try:
                        course: Course = Course.objects.get(course_id=sectioncourses[k].course_id_id)
                    except Course.DoesNotExist:
                        messages.error(request, 'Course not found')
                    else:
                        try:
                            professor = Professor.objects.get(professor_id=sectioncourses[k].professor_id_id)
                        except Professor.DoesNotExist:
                            messages.error(request, 'Professor not found')
                        else:
                            courseLecs = course.credit_hours
                            lecDuration = course.contact_hours / course.credit_hours
                            j = 0
                            while j < courseLecs:
                                lecFlag = True
                                if DupNum < workingHours + 5:
                                    if DupNum < 5:
                                        lecDay = random.randint(0, totalDays - 1)
                                        lecStartTime = random.randint(section.start_time, section.end_time - 1)
                                        if not lecStartTime <= section.end_time - lecDuration:
                                            lecFlag = False
                                    else:
                                        lecStartTime += 1
                                        if not lecStartTime <= section.end_time - lecDuration:
                                            lecDay = (lecDay + 1) % totalDays
                                            lecStartTime = section.start_time

                                    if lecFlag:
                                        if lecStartTime <= section.end_time - lecDuration:
                                            tot = 0
                                            while course.course_type != class_rooms[roomNum].TYPE or tot < totalRooms:
                                                roomNum = (roomNum + 1) % totalRooms
                                                tot += 1
                                            activityFlag = True
                                            activityID = [section.week_day[lecDay]] * int(lecDuration)
                                            for i in range(int(lecDuration)):
                                                activityID[i] += '-' + str(lecStartTime + i)
                                                # for activity in activities:
                                                if Activity.objects.filter(activity_id=activityID[i],
                                                                        class_id=section.class_id).count() != 0 or \
                                                        Activity.objects.filter(activity_id=activityID[i],
                                                                                professor_id=professor.professor_id).count() != 0 or \
                                                        Activity.objects.filter(activity_id=activityID[i],
                                                                                classroom_id=class_rooms[
                                                                                    roomNum].ID).count() != 0:
                                                    activityFlag = False
                                                    DupNum += 1
                                                # break
                                            if activityFlag:
                                                print('Activity generated')
                                                for i in range(int(lecDuration)):
                                                    newActivity = Activity(activity_id=activityID[i],
                                                                        activity_type='Replaceable',
                                                                        class_id=section.class_id,
                                                                        classroom_id=class_rooms[roomNum].ID,
                                                                        course_id=course.course_id,
                                                                        professor_id=professor.professor_id,
                                                                        day=section.week_day[lecDay],
                                                                        start_time=lecStartTime + i,
                                                                        end_time=lecStartTime + i + 1)
                                                    newActivity.save()
                                                    professor.available_hours = professor.available_hours - 1
                                                    professor.save()
                                                DupNum = 0
                                                j += 1
                                else:
                                    #Activity.objects.filter(class_id=section.class_id).delete()
                                    deleteActivities(id)
                                    messages.error(request, 'Solution does not exist.')
                                    DupNum +=1
                                    break
                messages.success(request, 'Timetable generated')
                #return redirect('timetable/')

            else:
                messages.error(request, 'Classroom does not exist.')
        else:
            messages.error(request, 'Courses does not exist.')
    except Class.DoesNotExist:
        messages.error(request, 'Class does not exist')
    
    
    sections = Class.objects.all()
    context = {'sections': sections}
    return render(request, 'timetableapp/ClassTable.html', context)



def deleteActivities(id):
    activities = list(Activity.objects.filter(class_id=id))
    for activity in activities:
        course = Course.objects.get(course_id=activity.course_id)
        professor = Professor.objects.get(professor_id=activity.professor_id)
        professor.available_hours += 1
        professor.save()
    Activity.objects.filter(class_id=id).delete()






@login_required(login_url='login')
def TimeTableView(request, id):
    try:
        section = Class.objects.get(class_id=id)
        courses = Course.objects.all()
        professors = Professor.objects.all()
        activities = Activity.objects.filter(class_id=id)
        rooms = Classroom.objects.all()
        time = [0] * (section.end_time - section.start_time)
        time_slot = [''] * (section.end_time - section.start_time)
        for x in range(0, len(time)):
            time_slot[x] = str(section.start_time + x) + ':00 - ' + str(section.start_time + x + 1) + ':00'
            time[x] = section.start_time + x
        context_1 = {'section': section, 'courses': courses, 'professors':professors, 'rooms': rooms, 
                     'activities': activities, 'time': time, 'time_slot': time_slot  }
        return render(request, 'timetableapp/TimeTable.html', context_1)
    except Class.DoesNotExist:
        messages.error(request, 'Activity does not exist')
    
        sections = Class.objects.all()
        context_2 = {'sections': sections}
        return render(request, 'timetableapp/ClassTable.html', context_2)