from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from .models import Student

from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .models import CustomGroupData, CustomGroup
from django import forms


admin.site.site_header = "PowerGrid"


# Register your models here.

class Math_Grade_10Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


class Math_Grade_9Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


class Math_Grade_11Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


class Math_Grade_12Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


admin.site.register(Math_Grade_9, Math_Grade_9Admin)
admin.site.register(Math_Grade_10, Math_Grade_10Admin)
admin.site.register(Math_Grade_11, Math_Grade_11Admin)
admin.site.register(Math_Grade_12, Math_Grade_12Admin)

class English_Grade_9Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]

class English_Grade_10Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


class English_Grade_11Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


class English_Grade_12Admin(admin.ModelAdmin):
    list_display = ('student', 'date', 'grade')
    list_filter = ["student", "date"]
    list_editable = ["grade"]


admin.site.register(English_Grade_9, English_Grade_9Admin)
admin.site.register(English_Grade_10, English_Grade_10Admin)
admin.site.register(English_Grade_11, English_Grade_11Admin)
admin.site.register(English_Grade_12, English_Grade_12Admin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'grade_level')
    list_filter = ["grade_level"]

admin.site.register(Student, StudentAdmin)

class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = '__all__'
        widgets = {
            'name': forms.Select(choices=GROUP_CHOICES),
        }

class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm

admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)



















class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'

class CustomUserAdmin(UserAdmin):
    inlines = [StudentInline]

# admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)