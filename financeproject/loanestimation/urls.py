
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loan_estimation, name='loan_estimation'),
]
