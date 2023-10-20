from django.db.models import *

from apps.plane.models import Plane

class Airplane(Model):

    title = CharField(verbose_name='Аэрапорт',max_length=256)
    data = DateField(verbose_name='дата вылета') 
    plane = ManyToManyField(Plane)

    def __str__(self):
        return f'{self.title}'
