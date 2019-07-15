from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studys/', views.StudyList.as_view()),
    path('study/<int:pk>/', views.study_detail),
]

# Allows use of .json or .api in request
urlpatterns = format_suffix_patterns(urlpatterns)