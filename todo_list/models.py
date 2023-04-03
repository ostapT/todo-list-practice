from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    complete = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return f"{self.content} {str(self.datetime)}"


class Tag(models.Model):
    name = models.ManyToManyField("Task")


