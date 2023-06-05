from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return self.title 
