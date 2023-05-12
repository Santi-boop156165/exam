from django.urls import path
from .views import ExamView

urlpatterns = [path('exam/',ExamView.as_view(), name="List Coffe")]