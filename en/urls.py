
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('ghar/' , views.ghar , name = 'ghar'),
    path('cv/' , views.cv , name='cv')
]
