import datetime
from xml.dom import ValidationErr
from django.db import models
from django.utils import timezone

from accounts.models import Employee

class EventManager(models.Manager):
    def create_event(self, **kwargs):
        if kwargs['start_time'] > kwargs['end_time']:
            raise ValidationErr('不正な開始終了時刻')
        return self.create(**kwargs)

class Event(models.Model):
    
    objects = EventManager()

    summary = models.CharField(
        verbose_name='概要',
        max_length=150
    )
    description = models.CharField(
        verbose_name='説明',
        max_length=800,
        blank=True
    )
    start_time = models.TimeField(
        verbose_name='開始時刻',
    )
    end_time = models.TimeField(
        verbose_name='終了時刻',
    )
    date = models.DateField(
        verbose_name='日付'
    )
    created_at = models.DateTimeField(
        verbose_name='作成日',
        default=timezone.now
    )
    author = models.OneToOneField(
        Employee,
        verbose_name='作成者',
        on_delete=models.SET_NULL,
        null=True,
        related_name='event_author'

    )
    participant = models.ForeignKey(
        Employee,
        verbose_name='参加者',
        on_delete=models.CASCADE,
        related_name='event_participant'
    )

    def __str__(self):
        return self.summary
    