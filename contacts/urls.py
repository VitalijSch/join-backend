from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreateContactView.as_view(), name='create'),
]
