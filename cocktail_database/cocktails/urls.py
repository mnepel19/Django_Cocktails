from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cocktails/<int:cocktail_id>/', views.detail, name="questions")
]