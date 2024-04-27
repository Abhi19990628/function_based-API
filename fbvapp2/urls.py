from django.urls import path
from .views import SchoolListView, SchooldetailsView

urlpatterns = [
    path('api/school/', SchoolListView, name='school-list'),
    path('api/school/<int:pk>/', SchooldetailsView, name='school-detail'),
]

