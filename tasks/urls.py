from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', views.TaskViewSet.as_view({'post': 'create'}), name='create'),
    path('detail/<slug:slug>/', views.TaskViewSet.as_view({'get': 'retrieve'}), name='detail'),
    path('update/<slug:slug>/', views.TaskViewSet.as_view({'patch': 'partial_update'}), name='update'),
    path('delete/<slug:slug>/', views.TaskViewSet.as_view({'delete': 'destroy'}), name='delete'),
]
