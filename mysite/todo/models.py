from django.db import models
from django.conf import settings


# Create your models here.


class TodoItem(models.Model):
    text = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ("change_todo_status", "Can change todo status"),
        ]
    def __str__(self):
        return f" ({self.text}) {self.author}"


