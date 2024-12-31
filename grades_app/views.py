from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Count, Avg
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import user_passes_test

import pdfkit
import csv

CustomUser = get_user_model()


# The Index Function
def index(request):


	user_groups = request.user.groups.values_list('name', flat=True)

	in_math_group = None
	in_english_group = None

	if 'High School Math Teachers' in user_groups:
		in_math_group = "High School Math Teachers"
	elif "High School English Teachers" in user_groups:
		in_english_group = 'High School English Teachers' in user_groups

	context = {
		
		'in_math_group': in_math_group,
		'in_english_group' : in_english_group,

	}
	return render(request, 'grades_app/index.html', context)

@login_required
def student_detail(request):
    if not request.user.is_staff:
        student = get_object_or_404(Student, user=request.user)
        return render(request, 'grades_app/student_detail.html', {'student': student})
    else:
        # Handle the case if the logged-in user is not a student
        return render(request, 'grades_app/access_denied.html')

@login_required
def subject_grades(request):
	student = request.user.student

	math_grade_of_student_9 = Math_Grade_9.objects.filter(student=student).aggregate(Avg('grade'))
	math_grade_of_student_10 = Math_Grade_10.objects.filter(student=student).aggregate(Avg('grade'))
	math_grade_of_student_11 = Math_Grade_11.objects.filter(student=student).aggregate(Avg('grade'))
	math_grade_of_student_12 = Math_Grade_12.objects.filter(student=student).aggregate(Avg('grade'))

	english_grade_of_student_9 = English_Grade_9.objects.filter(student=student).aggregate(Avg('grade'))
	english_grade_of_student_10 = English_Grade_10.objects.filter(student=student).aggregate(Avg('grade'))
	english_grade_of_student_11 = English_Grade_11.objects.filter(student=student).aggregate(Avg('grade'))
	english_grade_of_student_12 = English_Grade_12.objects.filter(student=student).aggregate(Avg('grade'))

	math_average_9 = math_grade_of_student_9["grade__avg"] 
	math_average_10 = math_grade_of_student_10["grade__avg"] 
	math_average_11 = math_grade_of_student_11["grade__avg"] 
	math_average_12 = math_grade_of_student_12["grade__avg"] 

	english_average_9 = english_grade_of_student_9["grade__avg"]
	english_average_10 = english_grade_of_student_10["grade__avg"]
	english_average_11 = english_grade_of_student_11["grade__avg"]
	english_average_12 = english_grade_of_student_12["grade__avg"]

	context = {

		"student": student,
		
		"math_grades_9" : Math_Grade_9.objects.filter(student=student).order_by("-date"),
		"math_grades_10" : Math_Grade_10.objects.filter(student=student).order_by("-date"),
		"english_grades_9" : English_Grade_9.objects.filter(student=student).order_by("-date"),
		"english_grades_10" : English_Grade_10.objects.filter(student=student).order_by("-date"),

		"math_average_9" : math_average_9,
		"math_average_10" : math_average_10,
		"math_average_11" : math_average_11,
		"math_average_12" : math_average_12,

		"english_average_9" : english_average_9,
		"english_average_10" : english_average_10,
		"english_average_11" : english_average_11,
		"english_average_12" : english_average_12,


	}
	return render(request, 'grades_app/list_grades.html', context)

def calculate_average_math_grade(student, grade_level):


    if grade_level == 9:
        grade_model = Math_Grade_9
    elif grade_level == 10:
        grade_model = Math_Grade_10
    elif grade_level == 11:
        grade_model = Math_Grade_11
    elif grade_level == 12:
        grade_model = Math_Grade_12
    else:
        return 0
    
    math_grades = grade_model.objects.filter(student=student)
    total_grades = math_grades.count()
    
    if total_grades > 0:
        total_sum = sum(grade.grade for grade in math_grades)
        average_grade = total_sum / total_grades
        return average_grade
    else:
        return 0

def calculate_average_english_grade(student, grade_level):


    if grade_level == 9:
        grade_model = English_Grade_9
    elif grade_level == 10:
        grade_model = English_Grade_10
    elif grade_level == 11:
        grade_model = English_Grade_11
    elif grade_level == 12:
        grade_model = English_Grade_12
    else:
        return 0
    
    english_grades = grade_model.objects.filter(student=student)
    total_grades = english_grades.count()
    
    if total_grades > 0:
        total_sum = sum(grade.grade for grade in english_grades)
        average_grade = total_sum / total_grades
        return average_grade
    else:
        return 0


@login_required
@user_passes_test(lambda user: user.groups.filter(name='High School Math Teachers').exists())
def math_average(request, grade_level):


	students = Student.objects.filter(grade_level=grade_level)
	student_grades_list = []

	grade_levels = [9, 10, 11, 12]

	for student in students:
		average_grade = calculate_average_math_grade(student, grade_level)
		student_grades_list.append((student.first_name, student.last_name, average_grade))

	context = {
		'student_grades_list': student_grades_list,
		'grade_level': grade_level,
		'grade_levels': grade_levels,
		
	}

	return render(request, 'grades_app/math_averages.html', context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='High School English Teachers').exists())
def english_average(request, grade_level):


	students = Student.objects.filter(grade_level=grade_level)
	student_grades_list_english = []

	grade_levels = [9, 10, 11, 12]

	for student in students:
		average_grade = calculate_average_english_grade(student, grade_level)
		student_grades_list_english.append((student.first_name, student.last_name, average_grade))

	grades_to_chart = []
	for grades in student_grades_list_english:
		# grades_to_chart = []
		whatever = grades[2]
		grades_to_chart.append(whatever)
	# print(grades_to_chart)
	grades_to_chart = grades_to_chart
		
		

	context = {
		'student_grades_list': student_grades_list_english,
		'grade_level': grade_level,
		'grade_levels': grade_levels,
		'grades_to_chart': grades_to_chart,
		
	}


	return render(request, 'grades_app/english_averages.html', context)


# All the Report generate functions

@login_required
@user_passes_test(lambda user: user.groups.filter(name='High School Math Teachers').exists())
def math_generate_report(request, grade_level):


	students = Student.objects.filter(grade_level=grade_level)
	student_grades_list = []

	grade_levels = [9, 10, 11, 12]

	for student in students:
		average_grade = calculate_average_math_grade(student, grade_level)
		student_grades_list.append((student.first_name, student.last_name, average_grade))
	
	


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = f'attachment; filename="Math Average Grade {grade_level}.csv"'

	# response = HttpResponse(content_type='text/csv', headers={'Content-Disposition': 'attachment; filename="Math_Average.csv"'},)
	writer = csv.writer(response)
	writer.writerow(['First Name', "Last Name", 'Average Grade',])

	for student in student_grades_list:
		writer.writerow([f"{student[0]}", f"{student[1]}", f"{student[2]}"])
	return response


@login_required
@user_passes_test(lambda user: user.groups.filter(name='High School English Teachers').exists())
def english_generate_report(request, grade_level):


	students = Student.objects.filter(grade_level=grade_level)
	student_grades_list = []

	grade_levels = [9, 10, 11, 12]

	for student in students:
		average_grade = calculate_average_english_grade(student, grade_level)
		student_grades_list.append((student.first_name, student.last_name, average_grade))
	
	


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = f'attachment; filename="English Average Grade {grade_level}.csv"'

	# response = HttpResponse(content_type='text/csv', headers={'Content-Disposition': 'attachment; filename="Math_Average.csv"'},)
	writer = csv.writer(response)
	writer.writerow(['First Name', "Last Name", 'Average Grade',])

	for student in student_grades_list:
		writer.writerow([f"{student[0]}", f"{student[1]}", f"{student[2]}"])
	return response

