from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('top-rated/', views.top_rated, name='top_rated'),
    path('upcoming/',views.upcoming, name='upcoming'),
    path('movie/<int:movie_id>/',views.movie_detail,name='movie_detail'),
    path('search/',views.search, name='search'),
]
