from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='compiler'),
    path('runcode', views.runcode, name='runcode'),
    path('save', views.save, name='save')

]
