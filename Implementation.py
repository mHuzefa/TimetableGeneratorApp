# importing modules to be used

import random

# Course class to save the details of course
class Course:
    def __init__(self, ID, Name, Type, LecturePerWeek, LectureLength):
        self.ID = ID
        self.Name = Name
        self.Type = Type
        self.LecPerWeek = LecturePerWeek
        self.LecDuration = LectureLength

    def printCourse(self):
        print("-----------------------------------")
        print("----------------Course-------------")
        print("-----------------------------------")
        print("ID: \n" + self.ID)
        print("Name: \n" + self.Name)
        print("Type: \n" + self.Type)
        print("Lectures in Week: ")
        print(self.LecPerWeek)
        print("Lecture Length: ")
        print(self.LecDuration)


# Teacher class to store details of a teacher
class Teacher:
    def __init__(self, ID, Name, PerWeekWorkingHrs, CourseList):
        self.ID = ID
        self.Name = Name
        self.PerWeekHrs = PerWeekWorkingHrs
        self.AvailableHours = PerWeekWorkingHrs
        self.CourseList = CourseList
        self.Availability = [[0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24]

    def setAvailHrs(self, hrs):
        self.AvailableHours = self.AvailableHours - hrs

    def printTeacher(self):
        print("-----------------------------------")
        print("-------------Teacher---------------")
        print("-----------------------------------")
        print("ID: \n" + self.ID)
        print("Name: \n" + self.Name)
        print("Working Hours in Week: ")
        print(self.PerWeekHrs)
        print("Available Hours in Week: ")
        print(self.AvailableHours)
        print("Course to Teach: ")
        for x in self.CourseList:
            print(x.ID)
        print("Availability")
        for x in self.Availability:
            print(x)


# ClassRoom class to store classroom details
class ClassRoom:
    def __init__(self):
        self.ID = None
        self.Name = None
        self.Type = None
        self.Availability = [[0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24]

    def __init__(self, ID, Name, Type):
        self.ID = ID
        self.Name = Name
        self.Type = Type
        self.Availability = [[0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24]

    def printClassRoom(self):
        print("-----------------------------------")
        print("-------------Class Room------------")
        print("-----------------------------------")
        print("ID: \n" + self.ID)
        print("Name: \n" + self.Name)
        print("Class room type: ")
        print(self.Type)
        print("Availability")
        for x in self.Availability:
            print(x)


# TimeTable class to save the prototype of timetable
class WeeklySchedule:
    def __init__(self, ID, perLecDuration, StartList, EndList):
        self.ID = ID
        self.perLecDuration = perLecDuration
        self.Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # StartList and EndList are List to store start and end
        # time of working hours of day sequentially from Monday
        self.StartList = StartList
        self.EndList = EndList

    def printWeeklySchedule(self):
        print("-----------------------------------")
        print("----------Weekly Schedule----------")
        print("-----------------------------------")
        print("ID:\n" + self.ID)
        print("Per Lecture Duration in Hours:")
        print(self.perLecDuration)
        for x in range(7):
            print("For Day of " + self.Days[x] + " Working hours start from:")
            print(self.StartList[x])
            print("Ends at:")
            print(self.EndList[x])


# Class class to store details of a class
class Class:
    def __init__(self, ID, Name, Session, Semester, WeekSchedule):
        self.ID = ID
        self.Name = Name
        self.Session = Session
        self.Semester = Semester
        self.WeekSchedule = WeekSchedule
        self.Availability = [[0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24]
        for i in range(7):
            for j in range(24):
                if j < WeekSchedule.StartList[i] - 1 or j > WeekSchedule.EndList[i] - 1:
                    self.Availability[i][j] = 1
        #self.Availability = [[0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24, [0]*24]

    def printClass(self):
        print("-----------------------------------")
        print("---------------Class---------------")
        print("-----------------------------------")
        print("ID: \n" + self.ID)
        print("Name: \n" + self.Name)
        print("WeeklySchedule ID: " + self.WeekSchedule.ID)
        print("Session: ")
        print(self.Session)
        print("Semester: ")
        print(self.Semester)
        print("Availability")
        for x in self.Availability:
            print(x)


#   [ClassID, CourseID, Day, startTime, EndTime, Teacher, ClassRoom]

# Activity class to store record of activity for a class
class Activity:
    def __init__(self):
        self.ID = None
        self.myClass = None
        self.myCourse = None
        self.Day = None
        self.lecStartTime = None
        self.lecEndTime = None
        self.myTeacher = None
        self.myClassroom = None

    def __init__(self, ID, myClass, myCourse, Day, lecStartTime, lecEndTime, myTeacher, myClassroom):
        self.ID = ID
        self.myClass = myClass
        self.myCourse = myCourse
        self.Day = Day
        self.lecStartTime = lecStartTime
        self.lecEndTime = lecEndTime
        self.myTeacher = myTeacher
        self.myClassroom = myClassroom

    def printActivity(self):
        print("-----------------------------------")
        print("-------------Activity--------------")
        print("-----------------------------------")
        print("ID: " + self.ID)
        print("Day: " + self.Day)
        print("Class:")
        print(self.myClass)
        print("Course:")
        print(self.myCourse)
        print("Teacher:")
        print(self.myTeacher)
        print("ClassRoom:")
        print(self.myClassroom)
        print("Start:")
        print(self.lecStartTime)
        print("End:")
        print(self.lecEndTime)
        print("-----------------------------------")


##  FixedLecList has following features
##  [[lecID, Day, start, end, teacher, lecRoom]]


def ActivityScheduling(Sec, CourseList, CRoomList, TeacherList, WeekSchedule, FixedLecList, ActivityList):
    # variable to save weekly working hours of class
    weekHours = 0
    # variable to save index of class room being used
    roomNum = 0
    lecDay = 0
    lecStartTime = 0
    # to set week hours variable
    for x in CourseList:
        weekHours += x.LecPerWeek * x.LecDuration
    # to keep track of num of activities
    ActivityNum = len(ActivityList)
    courseNum = 0
    DupNum = 0
    #doubleLecFlag = False
    for x in range(len(FixedLecList)):
        ActivityList.append(Activity(WeekSchedule.Days[FixedLecList[x][1]] + str(FixedLecList[x][2]), Sec,
                                     FixedLecList[x][0], WeekSchedule.Days[FixedLecList[x][1]], FixedLecList[x][2],
                                     FixedLecList[x][3], FixedLecList[x][4], FixedLecList[x][5]))
        Sec.Availability[FixedLecList[x][1]][FixedLecList[x][2] - 1] = 1
        if FixedLecList[x][4]:
            FixedLecList[x][4].Availability[FixedLecList[x][1]][FixedLecList[x][2]-1] = 1
            FixedLecList[x][4].setAvailHrs(1)
        if FixedLecList[x][5]:
            FixedLecList[x][5].Availability[FixedLecList[x][1]][FixedLecList[x][2]-1] = 1

    while courseNum < len(CourseList):
        j = 0
        while j < CourseList[courseNum].LecPerWeek:
            lecFlag = True
            if DupNum < 5:
                lecDay = random.randint(0, 4)

                lecStartTime = random.randint(WeekSchedule.StartList[lecDay], WeekSchedule.EndList[lecDay] - 1)
                if not lecStartTime <= WeekSchedule.EndList[lecDay] - CourseList[courseNum].LecDuration:
                    lecFlag = False
            else:
                lecStartTime += 1
                if not (lecStartTime < WeekSchedule.EndList[lecDay] and lecStartTime <=
                        WeekSchedule.EndList[lecDay] - CourseList[courseNum].LecDuration):
                    lecDay = (lecDay + 1) % 5
                    lecStartTime = WeekSchedule.StartList[lecDay]
                
            if lecFlag:
                if CourseList[courseNum].LecDuration <= WeekSchedule.EndList[lecDay] - lecStartTime:
                    while CourseList[courseNum].Type != CRoomList[roomNum].Type:
                        roomNum = (roomNum + 1) % len(CRoomList)
                       
                    activityFlag = True
                    for i in range(CourseList[courseNum].LecDuration):
                        if TeacherList[courseNum].Availability[lecDay][lecStartTime + i - 1] == 1 or\
                                CRoomList[roomNum].Availability[lecDay][lecStartTime + i - 1] == 1 or\
                                Sec.Availability[lecDay][lecStartTime + i - 1] == 1:
                            activityFlag = False
                            DupNum += 1
                    if activityFlag:
                        activityID = [WeekSchedule.Days[lecDay]] * CourseList[courseNum].LecDuration
                        for i in range(CourseList[courseNum].LecDuration):
                            activityID[i] += str(lecStartTime + i)
                            ActivityList.append(Activity(activityID[i], Sec.ID, CourseList[courseNum].ID,
                                                         WeekSchedule.Days[lecDay], lecStartTime + i,
                                                         lecStartTime + i + 1,
                                                         TeacherList[courseNum].ID, CRoomList[roomNum].ID))
                            TeacherList[courseNum].Availability[lecDay][lecStartTime + i - 1] = 1
                            CRoomList[roomNum].Availability[lecDay][lecStartTime + i - 1] = 1
                            Sec.Availability[lecDay][lecStartTime + i - 1] = 1

                            TeacherList[courseNum].setAvailHrs(1)
                            ActivityNum += 1
                            weekHours -= 1
                        j += 1
                        
        courseNum += 1

Classrooms = [ClassRoom] * 4
for i in Classrooms:
    i.ID = '7889'
    i.Name = 'HY'
    i.Type = 'LAB'

for i in Classrooms:
    i.printClassRoom()
# generating data 
MyCourses = [Course("CS104L", "OS", "Lab", 1, 3), Course("CS412L", "DB", "Lab", 1, 3),
             Course("CS311", "ALGO", "Theory", 3, 1), Course("CS404", "OS", "Theory", 3, 1),
             Course("CS412", "DB", "Theory", 3, 1), Course("CS421", "Calc", "Theory", 3, 1),
             Course("CS409", "Automata", "Theory", 3, 1)]

MyCourses[0].printCourse()

AlgoTeacher = Teacher("TID001", "Sammyan", 25, MyCourses)
DBTeacher = Teacher("TID002", "Dr.Awais", 25, MyCourses)
OSTeacher = Teacher("TID003", "Amna", 25, MyCourses)
CalcTeacher = Teacher("TID004", "Irfan", 25, MyCourses)
TATeacher = Teacher("TID005", "Touqir", 25, MyCourses)

MyTeachers = [OSTeacher, DBTeacher, AlgoTeacher, OSTeacher, DBTeacher, CalcTeacher, TATeacher]
AlgoTeacher.printTeacher()

RoomLT01 = ClassRoom("CSLT01", "N1", "Theory")

RoomLT01.printClassRoom()
RoomLT02 = ClassRoom("CSLT02", "N2", "Theory")

RoomDP01 = ClassRoom("CSDP", "LAB2", "Lab")

MySchedule = WeeklySchedule("WS001", 1, [8, 8, 8, 8, 8, 0, 0], [16, 16, 16, 16, 16, 0, 0])

SecAClass = Class("CS18A", "CS18_SecA", 2018, 4, MySchedule)
SecBClass = Class("CS18B", "CS18_SecB", 2018, 4, MySchedule)
SecCClass = Class("CS18C", "CS18_SecC", 2018, 4, MySchedule)
SecCEClass = Class("CS18CCE", "CS18_SecCCE", 2018, 4, MySchedule)


SecAClass.printClass()
SecBClass.printClass()
SecCClass.printClass()
SecCEClass.printClass()

#  FixedLecList has following features
#  [[lecName, Day, start, end, teacher, lecRoom]]

MyFixedLec = [["Break", 0, 12, 13, "", ""], ["Break", 1, 12, 13, "", ""], ["Break", 2, 12, 13, "", ""],
              ["Break", 3, 12, 13, "", ""], ["Break", 4, 12, 13, "", ""], ["Break", 4, 13, 14, "", ""]]

MySchedule.printWeeklySchedule()
MyActivities = []
print("***************************************************************************************************************")
print("_________________________________________________________________________________")
print("________________________________________1________________________________________")
print("_________________________________________________________________________________")
ActivityScheduling(SecAClass, MyCourses, [RoomLT01, RoomDP01], MyTeachers, MySchedule, MyFixedLec, MyActivities)
print("***************************************************************************************************************")
print("_________________________________________________________________________________")
print("________________________________________2________________________________________")
print("_________________________________________________________________________________")
ActivityScheduling(SecBClass, MyCourses, [RoomLT02, RoomDP01], MyTeachers, MySchedule, MyFixedLec, MyActivities)
print("***************************************************************************************************************")
print("_________________________________________________________________________________")
print("________________________________________3________________________________________")
print("_________________________________________________________________________________")
ActivityScheduling(SecCClass, MyCourses, [RoomLT01, RoomDP01, RoomLT02], MyTeachers, MySchedule, MyFixedLec, MyActivities)
print("***************************************************************************************************************")
print("_________________________________________________________________________________")
print("________________________________________4________________________________________")
print("_________________________________________________________________________________")
ActivityScheduling(SecCEClass, MyCourses, [RoomLT01, RoomDP01, RoomLT02], MyTeachers, MySchedule, MyFixedLec, MyActivities)
print("***************************************************************************************************************")


for k in range(len(MyActivities)):
    print("**********************************************")
    print("X = " + str(k))
    print("**********************************************")
    MyActivities[k].printActivity()

RoomLT01.printClassRoom()
#RoomLT02.printClassRoom()
RoomDP01.printClassRoom()
SecAClass.printClass()
#SecBClass.printClass()
#SecCClass.printClass()
#SecCEClass.printClass()

for x in MyTeachers:
    x.printTeacher()

