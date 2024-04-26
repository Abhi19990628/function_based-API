from django.urls import path
from .views import courseDetailView,courseListView

urlpatterns = [
    path('courses',courseListView),
    path('courses/<int:pk>',courseDetailView),
]
