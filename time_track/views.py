from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class HomeView(TemplateView):
    template_name = 'spa.html'


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
