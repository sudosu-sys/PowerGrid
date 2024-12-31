from django.db import models
from src.settings import AUTH_USER_MODEL
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

GROUP_CHOICES = (
    ('High School Math Teachers', _('High School Math Teachers')),
    ('High School English Teachers', _('High School English Teachers')),
    ('High School Chemistry Teachers', _('High School Chemistry Teachers')),
    ('High School Physics Teachers', _('High School Physics Teachers')),

    # Add more choices as needed
)

class CustomGroup(Group):
    class Meta:
        proxy = True
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name



    # Add any additional methods or properties as needed

class CustomGroupData(models.Model):
    group = models.OneToOneField(
        Group,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='custom_data'
    )
    name = models.CharField(_('name'), max_length=50, unique=True, choices=GROUP_CHOICES)

    # Add any additional fields or methods as needed

class Student(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade_level = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Math_Grade_9(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Math Grade 9"

    def __str__(self):
        return f"{self.grade}"

class Math_Grade_10(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Math Grade 10"

    def __str__(self):
        return f"{self.grade}"

class Math_Grade_11(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Math Grade 11"

    def __str__(self):
        return f"{self.grade}"

class Math_Grade_12(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Math Grade 12"

    def __str__(self):
        return f"{self.grade}"

class English_Grade_9(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "English Grade 9"

    def __str__(self):
        return f"{self.grade}"

class English_Grade_10(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "English Grade 10"

    def __str__(self):
        return f"{self.grade}"

class English_Grade_11(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "English Grade 11"

    def __str__(self):
        return f"{self.grade}"

class English_Grade_12(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,)
    date = models.DateField()
    grade = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "English Grade 12"


    def __str__(self):
        return f"{self.grade}"