from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='home'),
    path('cbvdelete/<str:name>/', views.CityDeleteView.as_view(),name='cbvdelete_city')
]