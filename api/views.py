from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import examSerializer
from .models import Exam
# Create your views here.


class ExamView(APIView):
    def get(self, request):
    
        exams = Exam.objects.all()

        serializer = examSerializer(exams, many=True)

        return Response(serializer.data)