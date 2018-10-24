from django.db import models
from django.forms import ModelForm


class Post(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Relationships
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # recursive relationship
    thread = models.ForeignKey('self', on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()
    birth_date = models.DateField()

    # Methods example
    def is_millennial(self):
        "Returns the whether the person is a millennial or not"
        import datetime
        return self.birth_date > datetime.date(1980)


# Inheritance
class Student(Person):
    gpa = models.FloatField()


# Meta example
class Goose(models.Model):
    weight = models.FloatField()

    class Meta:
        verbose_name_plural = 'geese'


# Model Forms
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'email', 'body']
