from rest_framework import serializers

from pkd.models import Pkd

class PkdSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pkd
       fields = ('pkdNumber', 'pkdDesc')