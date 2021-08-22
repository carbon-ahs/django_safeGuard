from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

from entity.models import Entity
class HumanResource(models.Model):
    entity = models.ForeignKey(Entity, on_delete=CASCADE)
    staff_num = IntegerField()
    worker_num = IntegerField()
    service_worker_num = IntegerField()
    other_num = IntegerField()
