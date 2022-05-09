from django.urls import path
from. import views


urlpatterns = [
    path('emp/', views.Employeedetails.as_view()),
    path('emp/<int:id>/', views.EmployeeInfo.as_view())
]