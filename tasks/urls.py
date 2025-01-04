from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', views.TaskViewSet.as_view({'post': 'create'}), name='create'),
]
