from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSets

router= DefaultRouter()

router.register(r'task',TaskViewSets)

urlpatterns = [
    path('',include(router.urls))
]
