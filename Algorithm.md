# Activity Selection Problem


### Description
##### According to the requirements, algorithm takes 6 parameters as input. We will discribe all of them a little bit to make better understanding of algorithm.  
##### First parameter is **Sec** which refers to the class for which we want to schedule timetable. Sec has different attributes i.e.  
- *ID* is uniqe for each class  
- *Name* may be unique  
- *Session* refers to grade of class  
- *Semester* refers to term in case of school  
- *WeekSchedule* (We will discribe it later) is a schedule prototype to be followed by class  
- *Availability* refers to the free slots of class in the working hours. **0** refers to empty slot while **1** refers to non empty solt  
##### Second parameter is **CourseList** which refers to the list of courses to be scheduled for **Sec**.Course has attributes i.e.  
- *ID* is uniqe for each course  
- *Name* may be unique  
- *Type* refers wheather it is Lab or Theory  
- *LecPerWeek* refers to number of lectures per week  
- *LecDuration* refers to time span of lecture  
##### Third parameter is **TeacherList** which refers to list of Teachers who will teach the courses in the **CourseList** to the **Sec** class.Teacher is associated with the course as TeacherList may contain same Teacher multiple times for different courses.Teacher has attributes i.e.  
- *ID* is uniqe for each teacher  
- *Name* may be unique  
- *perWeekHrs* refers to total working hours of a teacher in a week  
- *AvailableHours* refers to the remaining working hours for which no lectures are assigned yet  
- *CourseList* refers to the List of courses he/she can teach  
- *Availability* refers to the free slots of Teacher in the working hours. **0** refers to empty slot while **1** refers to non empty solt  
##### Fourth parameter is **CRoomList** which refers to List of Classrooms in which classes of specific course are to be scheduled.Classroom has attributes i.e.  
- *ID* is uniqe for each teacher  
- *Name* may be unique  
- *Type* refers wheather it is for Lab or Theory lectures  
- *Availability* refers to the free slots for Classroom. **0** refers to empty slot while **1** refers to non empty solt  
##### Fifth parameter is **WeekSchedule** which refers to the prototype for working hours of the whole week.To better understand, we need to see its attributes:  
- *ID* is uniqe for each WeekSchedule prototype  
- *perLecDuration* refers to the lecture spans for the week
- *Days* refer to the week days.
- *StartList* refers to the starting of working hours for each day  
- *EndList* refers to the Ending of working hours for each day  
##### Sixth parameter is **FixedLecList** which refers to a list which contains details of lectures or breaks to be fixed for **Sec** class.i.e  
*LecID, Day, Start, TeacherID, LecRoom*

#### Working of Algorithm:
For this algorithm, we have specific pre-conditions. i.e TeacherList is sorted with the ascending order of available hours of teachers to avoid conflicts.
**ActivityList** is the List of activities defined globaly. It contains all the activities of each class, teacher, courses associated with each classroom.
At the start of algorithm first we specify the fixed lecture/break slots. 


### Algorithm
```
#  FixedLecList has following elemnts
#  [[lecID, Day, start, teacher, lecRoom], ....]
def ActivityScheduling(Sec, CourseList, TeacherList, CRoomList, WeekSchedule, FixedLecList):

###### variable to be used
    roomNum = 0
    lecDay = 0
    lecStartTime = 0
    courseNum = 0
    DupNum = 0
    ##### Scheduling fixed activities
    for x in range(len(FixedLecList)):
        ##### call to the constructor of activity class to generate new activity
        ActivityList.append(Activity(WeekSchedule.Days[FixedLecList[x][1]] + str(FixedLecList[x][2]), Sec,
                                     FixedLecList[x][0], WeekSchedule.Days[FixedLecList[x][1]], FixedLecList[x][2],
                                     FixedLecList[x][2] + 1, FixedLecList[x][3], FixedLecList[x][4]))
                                     
        ##### filling slots for activities
        Sec.Availability[FixedLecList[x][1]][FixedLecList[x][2] - 1] = 1
        if FixedLecList[x][3]:
            FixedLecList[x][3].Availability[FixedLecList[x][1]][FixedLecList[x][2]-1] = 1
        if FixedLecList[x][4]:
            FixedLecList[x][4].Availability[FixedLecList[x][1]][FixedLecList[x][2]-1] = 1

    while courseNum < len(CourseList):
        ##### j is handling multiple lectures of a Subject
        j = 0   
        while j < CourseList[courseNum].LecPerWeek:
            lecFlag = True  ##### flag for setting activity
            if DupNum < 5:  ##### to avoid multiple random generation for single course
                ##### selecting random day
                lecDay = random.randint(0, len(WeekSchedule.StratList) - 1)
                ##### selecting random hour from working hours
                lecStartTime = random.randint(WeekSchedule.StartList[lecDay], WeekSchedule.EndList[lecDay] - 1)
                #### to check if lecture span exceeds the End time
                if not lecStartTime <= WeekSchedule.EndList[lecDay] - CourseList[courseNum].LecDuration:
                    lecFlag = False
            else:   ##### when randomized method does not give solution
                lecStartTime += 1
                if not (lecStartTime <= WeekSchedule.EndList[lecDay] - CourseList[courseNum].LecDuration):
                    lecDay = (lecDay + 1) % len(WeekSchedule.StratList)
                    lecStartTime = WeekSchedule.StartList[lecDay]
            ##### when lecuter span does not exceed End time then check for lecture duplication
            if lecFlag:
                    ##### selecting random room with the same type as compatible with course
                    while CourseList[courseNum].Type != CRoomList[roomNum].Type:
                        roomNum = random.randint(0, 100) % len(CRoomList)
                    activityFlag = True
                    ##### checking availability of slots for the complete lecture span
                    for x in range(CourseList[courseNum].LecDuration):
                        if TeacherList[courseNum].Availability[lecDay][lecStartTime + x - 1] == 1 or\
                                CRoomList[roomNum].Availability[lecDay][lecStartTime + x - 1] == 1 or\
                                Sec.Availability[lecDay][lecStartTime + x - 1] == 1:
                            DupNum += 1 ##### DupNum variable to avoid loop running
                            activityFlag = False
                     ##### when no activity is found duplicate
                    if activityFlag:
                        ##### setting activity id
                        activityID = [WeekSchedule.Days[lecDay]] * CourseList[courseNum].LecDuration
                        for x in range(CourseList[courseNum].LecDuration):
                            activityID[x] += str(lecStartTime + x)
                            apending array to store new activity
                            ActivityList.append(Activity(activityID[x], Sec.ID, CourseList[courseNum].ID,
                                                         WeekSchedule.Days[lecDay], lecStartTime + x,
                                                         lecStartTime + x + 1,
                                                         TeacherList[courseNum].ID, CRoomList[roomNum].ID))
                            ##### filling the slots to update availability
                            TeacherList[courseNum].Availability[lecDay][lecStartTime + x - 1] = 1
                            CRoomList[roomNum].Availability[lecDay][lecStartTime + x - 1] = 1
                            Sec.Availability[lecDay][lecStartTime + x - 1] = 1
                            TeacherList[courseNum].setAvailHrs(1)
                        j += 1
        courseNum += 1
```
