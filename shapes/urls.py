from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('draw_shape/', views.draw_shape, name='draw_shape'),
    path('update_floor/', views.update_floor, name='update_floor'),
    path('delete_shape/', views.delete_shape, name='delete_shape'),
    path('ideas/', views.ideas, name='ideas'),
]
