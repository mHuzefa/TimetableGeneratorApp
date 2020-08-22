# Correctness and Complexity of Algorithm


## Complexity of Algorithm

Suppose we have **T** number of teachers, **T** number of courses with **L** number of lectures per week lecture duration **X**, **C** number of classroom, **F** number of fixed lectures and **H** working hours for a class.


``
def ActivityScheduling(Sec, CourseList, TeacherList, CRoomList, WeekSchedule, FixedLecList):
 
###### variable to be used
    roomNum = 0
    lecDay = 0
    lecStartTime = 0
    courseNum = 0
    DupNum = 0
    ##### Scheduling fixed activities
    for x in range(len(FixedLecList)):      #### this loop runs **F** times
        ##### call to the constructor of activity class to generate new activity
        ActivityList.append(Activity(WeekSchedule.Days[FixedLecList[x][1]] + str(FixedLecList[x][2]), Sec,
                                     FixedLecList[x][0], WeekSchedule.Days[FixedLecList[x][1]], FixedLecList[x][2],
                                     FixedLecList[x][2] + 1, FixedLecList[x][3], FixedLecList[x][4]))
                                     
        ##### filling slots for activities
        Sec.Availability[FixedLecList[x][1]][FixedLecList[x][2] - 1] = 1
        if FixedLecList[x][3]:
            FixedLecList[x][3].Availability[FixedLecList[x][1]][FixedLecList[x][2]-1] = 1
            FixedLecList[x][4].setAvailHrs(1)
        if FixedLecList[x][4]:
            FixedLecList[x][4].Availability[FixedLecList[x][1]][FixedLecList[x][2]-1] = 1

    while courseNum < len(CourseList):  #### loop runs max T times
        ##### j is handling multiple lectures of a Subject
        j = 0   
        while j < CourseList[courseNum].LecPerWeek:     #### this loop running probability is L times
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
                    while CourseList[courseNum].Type != CRoomList[roomNum].Type:    #### loop runs max **Rand(C)** times
                        roomNum = random.randint(0, 100) % len(CRoomList)
                    activityFlag = True
                    ##### checking availability of slots for the complete lecture span
                    for x in range(CourseList[courseNum].LecDuration):       #### loop runs max **X** times
                        if TeacherList[courseNum].Availability[lecDay][lecStartTime + x - 1] == 1 or\
                                CRoomList[roomNum].Availability[lecDay][lecStartTime + x - 1] == 1 or\
                                Sec.Availability[lecDay][lecStartTime + x - 1] == 1:
                            DupNum += 1 ##### DupNum variable to avoid loop running
                            activityFlag = False
                     ##### when no activity is found duplicate
                    if activityFlag:
                        ##### setting activity id
                        activityID = [WeekSchedule.Days[lecDay]] * CourseList[courseNum].LecDuration
                        for x in range(CourseList[courseNum].LecDuration):   #### this loop runs max **X** times
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
``

### Discription:
    As we can see from above code that the complexity of algorithm is as follows:
       As we are following generating random slots, so the probability of loop **while j < CourseList[courseNum].LecPerWeek** depends upon Probability of scheduling L lectures.
       Same would be the case with the selection of Classroom.
#### Worst case would be:
       ** O(F + T * ( Prob(L) *( 2X + Prob(C) ) ) **
#### Best case would be:
       ** O(F + T * ( L * 2X ) ) **
#### Average case would be:
       O(F + 1/2 * T * ( 2X * ( Prob(L) + L ) + Prob(L) * Prob(C) ) )



## Correctness of Algorithm

### Description

##### Algorithm is iterative using one single for loop and two while loops nested. And we have to find the correctness of algorithm wheather with given any input we get the desired results. There are two ways of finding its correctness. 
- ##### Empirical Analysis
- #####   Formal Reasoning


### Empirical Analysis

An "Empirical"analysis is one based on actual experimentation and observation of results. We conducted the empirical analysis which provided us the desired result. But as we know it can not be the best way to find the correctness. <b>Experimental analysis will be provided at the end of the sheet to show the correctness of algorithm. </b>



### Formal Reasoning

Formal Reasoning is the best approach to find the algorithm correctness as it can give you a method to find correctness over the 'n' number of values. We have algorithm

       
        ActivityScheduling(Sec, CourseList, TeacherList, CRoomList, WeekSchedule, FixedLecList)

This is taking the 6 inputs, for sectionlist, courses list, teacher list, classrooms list, week based schedule that how many hours and how many days university will be open so according to that algorithm will decide and generate timetable and last one is a fixed lecture list which basically decides that when there will be no lecture in daily routine.


 ###### As we will breakdown our problem and will try to find the correctness and loop variant of each loop. 
 
  ######        variable to be used
    roomNum = 0
    lecDay = 0
    lecStartTime = 0
    courseNum = 0
    DupNum = 0

At start, we are fixing the values to <b>0</b>.

    Scheduling fixed activities
    for x in range(len(FixedLecList)):
        call to the constructor of activity class to generate new activity
        ActivityList.append(Activity(WeekSchedule.Days[FixedLecList[x][1]] + str(FixedLecList[x][2]), Sec,
                                     FixedLecList[x][0], WeekSchedule.Days[FixedLecList[x][1]], FixedLecList[x][2],
                                     FixedLecList[x][2] + 1, FixedLecList[x][3], FixedLecList[x][4]))
                                     
In our first <b>for loop</b>, we are scheduling the fixed activites. So our range is the length of fixed lectures which will be input in the function.

**Here we will do methematical induction.**

***STEP 1:***

        Step 1 is a base case when the value come into the for loop is 1.
        so for the first iteration if length of fixed lecture = 1 and x = 1, and loop terminates and base case is true.
***STEP 2:***
        
        now if the length of fixed lectures is n and x<n, as if the value goes greater than n then loop terminates. 
        In the loop activities are scheduling for n times.
                                array goes from x = 1 to n where FixLecList[k][Fixed Number]


Now, when our this loops terminates after scheduling the fixed activities, we move forward to the next nested while loop.

**Mathemaatical induction will be applied here too. But we will not go for first loop when the value entered in first loop index after that a nested while loop exists which will fulfill its condition first and then will come into parent loop and this will go on until the condition of first loop comes untrue. Our main purpose is finding the the loop invariants which will conclude our purpose by giving the correctness of algorithm over the while loop on any number course list given.**

        while courseNum < len(CourseList):
        ##### j is handling multiple lectures of a Subject
                j = 0   
                while j < CourseList[courseNum].LecPerWeek:
                
For the base case, when the loop start to iterate it goes to the nested loop before initializng the value of j to 0 which is handling the multiple lectures of a subject. It means that j will increment if the muliple lectures come.
In second loop, if j is less than the lectures hours of the course, loop will iterate until then. For example if any course has contact hour 3 and j = 0, so j<3 and loop will iterate again and when will same course come into loop, j will be 1. and it will iterate until j > course hours. 

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


But there is a problem here that course and day is selected randomly which means that finding correctness of this loop is difficult, as it does not give us loop invariants. But the empirical analysis of this algorithm gives the desired output.




## Output from the Empirical Analysis of Algorithm in High-Level Language.


                -----------------------------------
                ----------------Course-------------
                -----------------------------------
                ID: 
                CS104L
                Name: 
                OS
                Type: 
                Lab
                Lectures in Week: 
                1
                Lecture Length: 
                3
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID001
                Name: 
                Sammyan
                Working Hours in Week: 
                25
                Available Hours in Week: 
                25
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Class Room------------
                -----------------------------------
                ID: 
                CSLT01
                Name: 
                N1
                Class room type: 
                Theory
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                ---------------Class---------------
                -----------------------------------
                ID: 
                CS18A
                Name: 
                CS18_SecA
                WeeklySchedule ID: WS001
                Session: 
                2018
                Semester: 
                4
                Availability
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                -----------------------------------
                ---------------Class---------------
                -----------------------------------
                ID: 
                CS18B
                Name: 
                CS18_SecB
                WeeklySchedule ID: WS001
                Session: 
                2018
                Semester: 
                4
                Availability
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                -----------------------------------
                ---------------Class---------------
                -----------------------------------
                ID: 
                CS18C
                Name: 
                CS18_SecC
                WeeklySchedule ID: WS001
                Session: 
                2018
                Semester: 
                4
                Availability
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                -----------------------------------
                ---------------Class---------------
                -----------------------------------
                ID: 
                CS18CCE
                Name: 
                CS18_SecCCE
                WeeklySchedule ID: WS001
                Session: 
                2018
                Semester: 
                4
                Availability
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                -----------------------------------
                ----------Weekly Schedule----------
                -----------------------------------
                ID:
                WS001
                Per Lecture Duration in Hours:
                1
                For Day of Monday Working hours start from:
                8
                Ends at:
                16
                For Day of Tuesday Working hours start from:
                8
                Ends at:
                16
                For Day of Wednesday Working hours start from:
                8
                Ends at:
                16
                For Day of Thursday Working hours start from:
                8
                Ends at:
                16
                For Day of Friday Working hours start from:
                8
                Ends at:
                16
                For Day of Saturday Working hours start from:
                0
                Ends at:
                0
                For Day of Sunday Working hours start from:
                0
                Ends at:
                0
                *************************************
                ___________________________
                _____________1_____________
                ___________________________
                Total Activities
                0
                Activity Scheduled
                Activity Scheduled
                Activity Scheduled
                Activity Scheduled
                Activity Scheduled
                Activity Scheduled
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Week Hours:
                21
                CourseNum
                0
                Friday
                Lec Start Time:
                10
                room List while loop
                room count
                1
                room count
                1
                room found
                CSDP
                Dump
                1
                **************
                Activity Number = 0
                **************
                Week Hours:
                21
                CourseNum
                0
                Friday
                Lec Start Time:
                13
                room count
                1
                room found
                CSDP
                Dump
                2
                **************
                Activity Number = 0
                **************
                Week Hours:
                21
                CourseNum
                0
                Friday
                Lec Start Time:
                12
                room count
                1
                room found
                CSDP
                Dump
                3
                Dump
                4
                **************
                Activity Number = 0
                **************
                Week Hours:
                21
                CourseNum
                0
                Thursday
                Lec Start Time:
                12
                room count
                1
                room found
                CSDP
                Dump
                5
                **************
                Activity Number = 0
                **************
                Thursday
                Lec Start Time:
                13
                room count
                1
                room found
                CSDP
                **************
                Activity Number = 0
                **************
                Activity scheduling:
                Finally Activity scheduled:
                Activity scheduling:
                Finally Activity scheduled:
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=5
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Friday
                Lec Start Time:
                8
                room count
                1
                room found
                CSDP
                **************
                Activity Number = 3
                **************
                Activity scheduling:
                Finally Activity scheduled:
                Activity scheduling:
                Finally Activity scheduled:
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=5
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Friday
                Lec Start Time:
                9
                room List while loop
                room count
                0
                room count
                0
                room found
                CSLT01
                Dump
                6
                **************
                Activity Number = 6
                **************
                Friday
                Lec Start Time:
                10
                room count
                0
                room found
                CSLT01
                Dump
                7
                **************
                Activity Number = 6
                **************
                Friday
                Lec Start Time:
                11
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 6
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=7
                Friday
                Lec Start Time:
                12
                room count
                0
                room found
                CSLT01
                Dump
                8
                **************
                Activity Number = 7
                **************
                Friday
                Lec Start Time:
                13
                room count
                0
                room found
                CSLT01
                Dump
                9
                **************
                Activity Number = 7
                **************
                Friday
                Lec Start Time:
                14
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 7
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                2
                DupNum=9
                Friday
                Lec Start Time:
                15
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 8
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                3
                DupNum=9
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Monday
                Lec Start Time:
                8
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 9
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=9
                Monday
                Lec Start Time:
                9
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 10
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                2
                DupNum=9
                Monday
                Lec Start Time:
                10
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 11
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                3
                DupNum=9
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Monday
                Lec Start Time:
                11
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 12
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=9
                Monday
                Lec Start Time:
                12
                room count
                0
                room found
                CSLT01
                Dump
                10
                **************
                Activity Number = 13
                **************
                Monday
                Lec Start Time:
                13
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 13
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                2
                DupNum=10
                Monday
                Lec Start Time:
                14
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 14
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                3
                DupNum=10
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Monday
                Lec Start Time:
                15
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 15
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=10
                Tuesday
                Lec Start Time:
                8
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 16
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                2
                DupNum=10
                Tuesday
                Lec Start Time:
                9
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 17
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                3
                DupNum=10
                -----------------------------------
                ------------while Loop-------------
                -----------------------------------
                Tuesday
                Lec Start Time:
                10
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 18
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                1
                DupNum=10
                Tuesday
                Lec Start Time:
                11
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 19
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                2
                DupNum=10
                Tuesday
                Lec Start Time:
                12
                room count
                0
                room found
                CSLT01
                Dump
                11
                **************
                Activity Number = 20
                **************
                Tuesday
                Lec Start Time:
                13
                room count
                0
                room found
                CSLT01
                **************
                Activity Number = 20
                **************
                Activity scheduling:
                Finally Activity scheduled:
                J*****
                3
                DupNum=11
                Hello
                *************************************
                ___________________________
                _____________2_____________
                ___________________________
                *************************************
                ___________________________
                _____________3_____________
                ___________________________
                *************************************
                ___________________________
                _____________4_____________
                ___________________________
                *************************************
                ****************
                X = 0
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday12
                Day: Monday
                Class:
                <_main_.Class object at 0x03A58F58>
                Course:
                Break
                Teacher:

                ClassRoom:

                Start:
                12
                End:
                13
                -----------------------------------
                ****************
                X = 1
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Tuesday12
                Day: Tuesday
                Class:
                <_main_.Class object at 0x03A58F58>
                Course:
                Break
                Teacher:

                ClassRoom:

                Start:
                12
                End:
                13
                -----------------------------------
                ****************
                X = 2
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Wednesday12
                Day: Wednesday
                Class:
                <_main_.Class object at 0x03A58F58>
                Course:
                Break
                Teacher:

                ClassRoom:

                Start:
                12
                End:
                13
                -----------------------------------
                ****************
                X = 3
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Thursday12
                Day: Thursday
                Class:
                <_main_.Class object at 0x03A58F58>
                Course:
                Break
                Teacher:

                ClassRoom:

                Start:
                12
                End:
                13
                -----------------------------------
                ****************
                X = 4
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday12
                Day: Friday
                Class:
                <_main_.Class object at 0x03A58F58>
                Course:
                Break
                Teacher:

                ClassRoom:

                Start:
                12
                End:
                13
                -----------------------------------
                ****************
                X = 5
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday13
                Day: Friday
                Class:
                <_main_.Class object at 0x03A58F58>
                Course:
                Break
                Teacher:

                ClassRoom:

                Start:
                13
                End:
                14
                -----------------------------------
                ****************
                X = 6
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Thursday13
                Day: Thursday
                Class:
                CS18A
                Course:
                CS104L
                Teacher:
                TID003
                ClassRoom:
                CSDP
                Start:
                13
                End:
                14
                -----------------------------------
                ****************
                X = 7
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Thursday14
                Day: Thursday
                Class:
                CS18A
                Course:
                CS104L
                Teacher:
                TID003
                ClassRoom:
                CSDP
                Start:
                14
                End:
                15
                -----------------------------------
                ****************
                X = 8
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Thursday15
                Day: Thursday
                Class:
                CS18A
                Course:
                CS104L
                Teacher:
                TID003
                ClassRoom:
                CSDP
                Start:
                15
                End:
                16
                -----------------------------------
                ****************
                X = 9
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday8
                Day: Friday
                Class:
                CS18A
                Course:
                CS412L
                Teacher:
                TID002
                ClassRoom:
                CSDP
                Start:
                8
                End:
                9
                -----------------------------------
                ****************
                X = 10
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday9
                Day: Friday
                Class:
                CS18A
                Course:
                CS412L
                Teacher:
                TID002
                ClassRoom:
                CSDP
                Start:
                9
                End:
                10
                -----------------------------------
                ****************
                X = 11
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday10
                Day: Friday
                Class:
                CS18A
                Course:
                CS412L
                Teacher:
                TID002
                ClassRoom:
                CSDP
                Start:
                10
                End:
                11
                -----------------------------------
                ****************
                X = 12
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday11
                Day: Friday
                Class:
                CS18A
                Course:
                CS311
                Teacher:
                TID001
                ClassRoom:
                CSLT01
                Start:
                11
                End:
                12
                -----------------------------------
                ****************
                X = 13
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday14
                Day: Friday
                Class:
                CS18A
                Course:
                CS311
                Teacher:
                TID001
                ClassRoom:
                CSLT01
                Start:
                14
                End:
                15
                -----------------------------------
                ****************
                X = 14
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Friday15
                Day: Friday
                Class:
                CS18A
                Course:
                CS311
                Teacher:
                TID001
                ClassRoom:
                CSLT01
                Start:
                15
                End:
                16
                -----------------------------------
                ****************
                X = 15
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday8
                Day: Monday
                Class:
                CS18A
                Course:
                CS404
                Teacher:
                TID003
                ClassRoom:
                CSLT01
                Start:
                8
                End:
                9
                -----------------------------------
                ****************
                X = 16
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday9
                Day: Monday
                Class:
                CS18A
                Course:
                CS404
                Teacher:
                TID003
                ClassRoom:
                CSLT01
                Start:
                9
                End:
                10
                -----------------------------------
                ****************
                X = 17
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday10
                Day: Monday
                Class:
                CS18A
                Course:
                CS404
                Teacher:
                TID003
                ClassRoom:
                CSLT01
                Start:
                10
                End:
                11
                -----------------------------------
                ****************
                X = 18
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday11
                Day: Monday
                Class:
                CS18A
                Course:
                CS412
                Teacher:
                TID002
                ClassRoom:
                CSLT01
                Start:
                11
                End:
                12
                -----------------------------------
                ****************
                X = 19
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday13
                Day: Monday
                Class:
                CS18A
                Course:
                CS412
                Teacher:
                TID002
                ClassRoom:
                CSLT01
                Start:
                13
                End:
                14
                -----------------------------------
                ****************
                X = 20
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday14
                Day: Monday
                Class:
                CS18A
                Course:
                CS412
                Teacher:
                TID002
                ClassRoom:
                CSLT01
                Start:
                14
                End:
                15
                -----------------------------------
                ****************
                X = 21
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Monday15
                Day: Monday
                Class:
                CS18A
                Course:
                CS421
                Teacher:
                TID004
                ClassRoom:
                CSLT01
                Start:
                15
                End:
                16
                -----------------------------------
                ****************
                X = 22
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Tuesday8
                Day: Tuesday
                Class:
                CS18A
                Course:
                CS421
                Teacher:
                TID004
                ClassRoom:
                CSLT01
                Start:
                8
                End:
                9
                -----------------------------------
                ****************
                X = 23
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Tuesday9
                Day: Tuesday
                Class:
                CS18A
                Course:
                CS421
                Teacher:
                TID004
                ClassRoom:
                CSLT01
                Start:
                9
                End:
                10
                -----------------------------------
                ****************
                X = 24
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Tuesday10
                Day: Tuesday
                Class:
                CS18A
                Course:
                CS409
                Teacher:
                TID005
                ClassRoom:
                CSLT01
                Start:
                10
                End:
                11
                -----------------------------------
                ****************
                X = 25
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Tuesday11
                Day: Tuesday
                Class:
                CS18A
                Course:
                CS409
                Teacher:
                TID005
                ClassRoom:
                CSLT01
                Start:
                11
                End:
                12
                -----------------------------------
                ****************
                X = 26
                ****************
                -----------------------------------
                -------------Activity--------------
                -----------------------------------
                ID: Tuesday13
                Day: Tuesday
                Class:
                CS18A
                Course:
                CS409
                Teacher:
                TID005
                ClassRoom:
                CSLT01
                Start:
                13
                End:
                14
                -----------------------------------
                -----------------------------------
                -------------Class Room------------
                -----------------------------------
                ID: 
                CSLT01
                Name: 
                N1
                Class room type: 
                Theory
                Availability
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Class Room------------
                -----------------------------------
                ID: 
                CSDP
                Name: 
                LAB2
                Class room type: 
                Lab
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                ---------------Class---------------
                -----------------------------------
                ID: 
                CS18A
                Name: 
                CS18_SecA
                WeeklySchedule ID: WS001
                Session: 
                2018
                Semester: 
                4
                Availability
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                13
                3
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID003
                Name: 
                Amna
                Working Hours in Week: 
                25
                Available Hours in Week: 
                19
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID002
                Name: 
                Dr.Awais
                Working Hours in Week: 
                25
                Available Hours in Week: 
                19
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID001
                Name: 
                Sammyan
                Working Hours in Week: 
                25
                Available Hours in Week: 
                22
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID003
                Name: 
                Amna
                Working Hours in Week: 
                25
                Available Hours in Week: 
                19
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID002
                Name: 
                Dr.Awais
                Working Hours in Week: 
                25
                Available Hours in Week: 
                19
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID004
                Name: 
                Irfan
                Working Hours in Week: 
                25
                Available Hours in Week: 
                22
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                -----------------------------------
                -------------Teacher---------------
                -----------------------------------
                ID: 
                TID005
                Name: 
                Touqir
                Working Hours in Week: 
                25
                Available Hours in Week: 
                22
                Course to Teach: 
                CS104L
                CS412L
                CS311
                CS404
                CS412
                CS421
                CS409
                Availability
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

