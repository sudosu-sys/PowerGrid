from django.urls import path
from . import views 

app_name = "grades_app"

urlpatterns = [

	path('', views.index, name="index"),
	path('grades_app/<int:student_id>/', views.student_detail, name='student_detail'),
	path("grades", views.subject_grades, name="subject_grades"),

	# path("grade_choice", views.grade_choice, name="grade_choice"),
	# path("math_averages_9", views.math_averages_9, name="average_list_9"),
	# path("math_averages_10", views.math_averages_10, name="average_list_10"),

	path("math_average/<int:grade_level>", views.math_average, name="math_average"),
	path("english_average/<int:grade_level>", views.english_average, name="english_average"),

	path("math_generate_report/<int:grade_level>", views.math_generate_report, name="math_generate_report"),
	path("english_generate_report/<int:grade_level>", views.english_generate_report, name="english_generate_report"),
	# path("en_chart", views.en_chart, name="en_chart"),




]