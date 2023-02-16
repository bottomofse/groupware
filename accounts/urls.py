from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.CustomLoginView.as_view()),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLoginView.as_view(), name='logout'),
]