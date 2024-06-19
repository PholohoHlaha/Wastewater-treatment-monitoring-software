from django.urls import path
from . import views 


urlpatterns = [
    path("", views.analysis1, name='analysis1'),
    path("", views.analysis2, name='analysis2')
]