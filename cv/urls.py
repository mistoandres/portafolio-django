from django.urls import path
from .views import render_cv

urlpatterns = [
    path('', render_cv, name='cv')
]
