from .models import Message
from rest_framework import serializers


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at']