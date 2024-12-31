# from django.contrib import admin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

# # Register your models here.

# CustomUser = get_user_model()
# class CustomUserAdmin(UserAdmin):
# 	add_form = CustomUserCreationForm
# 	form = CustomUserChangeForm
# 	model = CustomUser
# 	list_display = ['email', 'username',]

# admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from grades_app.models import Student
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', "first_name", 'username', ]
    list_display_links = ('username', "first_name", 'email')
    inlines = [StudentInline]

admin.site.register(CustomUser, CustomUserAdmin)