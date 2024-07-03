from django.contrib import admin
from django.urls import path
from elixirapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('gallery/', views.gallery),
    path('info/', views.information),
    path('assinfo/', views.table2),
    path('regi/', views.regi),
    path('login/', views.login),
]
