from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    ITEM_STATUS_CHOICES = [
        ('생성', '생성'),
        ('대기', '대기'),
        ('실행중', '실행중'),
        ('완료', '완료'),
    ]

    item_text = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=ITEM_STATUS_CHOICES, default='생성')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item_text