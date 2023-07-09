from rest_framework import serializers
from api.models import * 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['created_at', 'updated_at']
        # fields  = "__all__"