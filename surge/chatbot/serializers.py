from rest_framework import routers, serializers, viewsets
from .models import History

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['conversation', 'created_at']
