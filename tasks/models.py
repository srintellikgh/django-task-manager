from django.db import models
from django.utils import timezone

from users.models import Person


class Task(models.Model):
    priority = models.CharField(max_length=3, choices=(
                                    ('LOW', 'Low'),
                                    ('MED', 'Medium'),
                                    ('HIG', 'High'),
                                    ('CRI', 'Critical'),
                                ), default='LOW',)

    assigned_employee = models.ForeignKey(Person, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    productivity_index = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return "/tasks/"
