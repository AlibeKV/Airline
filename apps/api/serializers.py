from rest_framework.serializers import *

from apps.airline.models import Airplane

from apps.plane.models import Plane

class Airplaneserializer(ModelSerializer):

    class Meta:

        model = Airplane
        fields = '__all__'


class PlaneSerializer(ModelSerializer):

    class Meta:

        model = Plane
        fields = '__all__'