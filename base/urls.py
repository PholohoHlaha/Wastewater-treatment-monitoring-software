from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),  
    path('lab_department/', include("lab_department.urls")),
    path('operators/', include("operators.urls")),
    path('analysis/', include("analysis.urls")),
    path('predict/', include("machine_learning.urls")),
]
