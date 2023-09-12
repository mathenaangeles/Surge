from rest_framework import routers, serializers, viewsets
from .models import History

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['conversation', 'sources', 'questions', 'created_at']
