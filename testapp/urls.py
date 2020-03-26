from django.urls import path
from .views import *

urlpatterns = [
    path('', TestView.as_view()),
    path('<int:id>', TestDetails.as_view()),
]