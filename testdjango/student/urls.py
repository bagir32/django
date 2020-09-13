from django.urls import path
from . import views
# this is url 
urlpatterns = [
    path('', views.student_show, name='student_show'), 
]