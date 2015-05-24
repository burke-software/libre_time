from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from time_track.views import HomeView, TaskViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
