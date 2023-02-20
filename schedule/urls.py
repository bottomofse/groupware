from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('',views.MonthCalendar.as_view(), name='month'),
    path('<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
]
