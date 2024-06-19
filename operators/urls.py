from django.urls import path
from . import views


urlpatterns = [
    path("",views.operator, name="app-landing-page")
]