from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addContact, name='add'),
    path('complete/<Contact_id>', views.completeContact, name='complete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    ]