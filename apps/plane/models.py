from django.db.models import *

class Plane(Model):

    title = CharField(verbose_name='Самолет',max_length=256)
    compile = CharField(verbose_name='характеристика',max_length=256) 
    capacity = IntegerField(verbose_name='вместимость')
    
    
    def __str__(self):
        return f'{self.title}'


