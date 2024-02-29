from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course_img = models.ImageField(default='default.jpg',upload_to='course_images')
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title