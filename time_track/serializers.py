from rest_framework import serializers
from .models import Task, Entry


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
