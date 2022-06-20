from django.urls import path
from .views import EmpListView

urlpatterns = [
    path('home/',EmpListView.as_view())
    ]