from django.db import models

from user.models import User


class Course(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    teacher = models.ForeignKey(User, null=False, blank=False, related_name='courses',
                                on_delete=models.CASCADE)
    time = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    content_titles = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,
                                related_name='student_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False,
                               related_name='student_courses')

    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name + ' - ' + self.course.name
