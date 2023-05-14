from django.db import models

# Create your models here.
class Todo_List(models.Model):
    title = models.CharField(max_length=200)  # Title of todo item
    description = models.TextField()   # Description and additional details of the todo item
    created = models.DateTimeField(auto_now_add=True)   # when the item is created
    completed = models.BooleanField(default=False)    # indicate whether the item has been completed or not

    def __str__(self):
        return self.title



