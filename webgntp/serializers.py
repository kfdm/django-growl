from rest_framework import serializers
from webgntp.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'application', 'notification', 'type', 'meta')
        read_only_fields = ('id',)
