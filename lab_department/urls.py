from django.urls import path
from . import views 


urlpatterns = [
    path("",views.index, name="app-landing-page"),
    path("login_view/", views.login_view, name = "login"),
    path('tertiary_view/', views.tertiary_view, name='tertiary'),
    path('secondary_view/', views.secondary_view, name='secondary'),
    path('primary_view/', views.primary_view, name='primary'),
    path('primary_analysis/', views.primary_analys, name='primaryA'),
    path('secondary_analysis/',views.secondary_analys, name='secondaryA'),
    path('tertiary/', views.tertiary_analys, name='tertiaryA'),
    path('predict/', views.predict_view, name= 'predict')
]