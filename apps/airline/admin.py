from django.contrib.admin import *

from .models import Airplane
@register(Airplane)
class AirplaneAdmin(ModelAdmin):

    list_display = ('id','title')
    list_display_links = ('id','title')
