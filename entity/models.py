from django.db import models

class Entity(models.Model):
    industrial = 'in'
    residential = 'rs'
    commercial = 'cm'
    entity_type_choices = [
        (industrial, 'Industrial'),
        (industrial, 'Commercial but using as industrial'),
        (commercial, 'Commercial'),
        (commercial, 'Residential but using as commercial'),
        (residential, 'Residential'),
        
    ]
    type = models.CharField(max_length=2, choices=entity_type_choices)

    def __str__(self):
        return str(self.id) + ' ' + self.type
    