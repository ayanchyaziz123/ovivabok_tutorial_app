from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.course_name

class Tutorial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tutorial_title = models.CharField(max_length=200)
    tutorial_description = RichTextField()
    tutorial_image = models.ImageField(upload_to='tutorial_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    is_public = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.tutorial_title

