from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.BoardView.as_view(), name='board'),
    path('<int:pk>/', views.PostView.as_view(), name='post_detail'),
]