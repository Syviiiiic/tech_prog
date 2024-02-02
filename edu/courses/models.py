from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, 
                                related_name='courses',
                                on_delete=models.CASCADE)
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title



class Module(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, 
                               related_name='modules',
                               on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


