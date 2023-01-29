from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listcomic, name = 'view')
    # path('', views.listmember)
]