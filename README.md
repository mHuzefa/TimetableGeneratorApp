# Timetable Generator Web-Application
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)        ![Django](https://img.shields.io/badge/Made%20with-Django-blue?style=?style=plastic&logo=appveyor&logo=data:image/png;base64)

###### This was final project with ![Abdullah Saleem](https://github.com/mrabdullahdev) for Analysis of Algorithm in Semester 4

This is the Activity Scheduling Ptoject which will generate the timetable of different sections for user with required inputs.

## Configuration Setup
<b>Project Configuration Guidelines(Step by Step):</b>

To run this project on your local server, follow the following steps:
* Install Python 3.8 on your Computer from the official website.
* Install Django on your computer by running this command 
                      
                      pip install Django(For windows)   
                      python -m pip install Django(For Mac/Linux)

* Install Django Crispy Forms by running this command:

                      pip install django-crispy-forms
* Install Django Multi select fields on your computer:

                      pip install django-multiselectfield
* If you don’t have Git Bash/Git Bucket on your computer. Then install it first.
* Run this command on your git terminal

                      git clone “https://github.com/mHuzefa/TimetableGeneratorApp.git”
* After clonning the repository in your computer, run the command:

                      cd TimetableGeneratorApp
* Run this command to run server on your localhost:8000

                       python manage.py runserver
- App is running on your Computer now. Enjoy!!!








## Alogrithm
When first we started the project we chosed the Greedy algorithm to perform for our project but as days went by, we could not complete it in greedy way so the most suitable approach we reached, was <b>Randomized Brute Force</b> as some of the values generated in algorithm was random in order to fulfill the requirements. This algorithm is connected with the database in the back-end where the data saved in the database will be passed through the algorithm to generate the timetable. Our Algorithm on the console is just working perfectly but as we were learning the python and Django for the first time so that got us into the problem to connect the database with the algorithm but we are working on it untill we have time.

## Features
1. User-Friendly GUI which helps you upload data on the go.
2. You can generate timetable for one class at a time.
3. You can download the PDF file of the timetable.
4. A responsive app which can be used in any device.

## Quick Demo   
![Quick Demo](https://github.com/mrabdullahdev/CS311S20PID27/blob/master/Home%20-%20Activity%20Scheduling%20App.webm%20-%20Google%20Drive.gif "Quick Demo of website")

## Desktop View
![Desktop View](Screenshots/main-page.png "Main Page")
## Mobile View
![Mobile View](Screenshots/mobile-view.png "Mobile View - Responsive")
## Timetable
![Timetable](Screenshots/Timetable.png "Timetable")
## Course Interface
![Add Course](Screenshots/Add-Course.png "Add Course")

## Professor Interface
![Add Professor](Screenshots/Add-Professor.png "Add Professor")
## Classroom Interface
![Add Classroom](Screenshots/Add-classroom.png "Add Classroom")

## Class(Section) Interface
![Add Section](Screenshots/add-Class.png "Add Section")


## View Table Interface
![View Table](Screenshots/Professo-Table.png "View Table")

![View Table2](Screenshots/Class-Table.png "Class table")



## Update Page Interface
![update page](Screenshots/update.png "Update Page")


## Delete Page Interface
![Delete Page](Screenshots/delete.png "delete page")


## User Interface Change Request
When we are asked to make the user interface of your app in just few days, we made the interface as best as we can in that short time. But as we started working on project, our interface was not user friendly which was our first priority. So we imporved our version of this interface which is shown below to the version which you can watch now. We have tried our best to make the interface as friendly as we could. [Here](https://github.com/mrabdullahdev/CS311S20PID27/blob/master/Activity%20Scheduling%20-%20Final%20Project-compressed_2.pdf) you can see the old user-interface.

![Old-Prototype](https://github.com/mrabdullahdev/CS311S20PID27/blob/master/Activity%20Scheduling%20(Prototyping).PNG "Old Prototype of App")
