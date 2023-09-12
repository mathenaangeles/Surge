from django.db import models
import json
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class History(models.Model):
    conversation = models.JSONField()
    sources = ArrayField(models.CharField(max_length=256), default=list)
    questions = ArrayField(models.CharField(max_length=256),size=3, default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps(self.conversation)
    
    class Meta:
        verbose_name_plural = "Histories"