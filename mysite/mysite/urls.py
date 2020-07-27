from django.contrib import admin
from django.urls import path

from vue_app import views as vue_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', vue_views.test_vue),
]
