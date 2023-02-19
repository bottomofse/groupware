from django.db import models
from django.db.models import Max

class GroupwareFunction(models.Model):
    title = models.CharField(max_length=150)
    # URL逆引用
    path_index = models.CharField(max_length=500)
    # 並び順の優先度
    order_priority = models.IntegerField(default=999)
