from django.urls import path
from . import views


urlpatterns = [
    path('cus/',views.CustomerDetails.as_view()),
    path('cus/<int:id>/', views.CustomerInfo.as_view())
]