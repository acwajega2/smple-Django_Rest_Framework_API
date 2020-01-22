from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from movies import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movie/', views.MovieList.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)