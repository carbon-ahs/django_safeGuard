from django.db import models
from django.db.models.deletion import CASCADE
from entity.models import Entity

class Building(models.Model):
    rented = 'rt'
    owned = 'on'
    building_type_choices = [
        (rented, 'Rented'),
        (owned, 'Owned'),
    ]
    entity = models.ForeignKey(Entity, on_delete=CASCADE)

    type = models.CharField(max_length=2, choices=building_type_choices)
    total_floors = models.IntegerField()
    total_floor_area = models.IntegerField()
    height = models.FloatField()

    def __str__(self):
        return 'Building ' + str(self.id) + ' ' + self.entity.type
    
    