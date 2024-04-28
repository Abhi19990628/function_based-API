from django .urls import path 
from .views import StudentDetailList,StudentViewList

urlpatterns = [
    path('student/', StudentViewList , name='Student-List'),
    path('student/<int:pk>/', StudentDetailList , name='Student-Detail')
]
