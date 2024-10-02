from django.urls import path
from . import views
from . views import VideoView

urlpatterns = [
    path('', views.home_page),
    path('audio/',VideoView.as_view()),
]
