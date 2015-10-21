from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('id', 'title','completed', 'order')
