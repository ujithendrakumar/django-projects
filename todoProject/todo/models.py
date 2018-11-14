from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.name
