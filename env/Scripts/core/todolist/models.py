from django.db import models

class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    status_choices = [
        ('CREATED', 'Created'),
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='CREATED')

    def __str__(self):
        return self.item_text
