from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path(r'^upvote/(?P<kind_id>[0-9]+)/$', views.upvote, name='upvote'),
    path('admin-edit/', views.admin, name='admin'),
    path('delete/', views.delete, name='delete'),
]
