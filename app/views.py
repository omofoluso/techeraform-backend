from django.shortcuts import render
from rest_framework import generics
from .models import ProgramApplication
from .serializer import ProgramApplicationSerializer
from .utils import send_registration_email
# Create your views here.

class ProgramApplicationListCreate(generics.ListCreateAPIView):
    queryset = ProgramApplication.objects.all()
    serializer_class = ProgramApplicationSerializer

    def perform_create(self, serializer):
        #save the new student info
        instance = serializer.save()

        send_registration_email(instance.email, instance.first_name)

class ProgramApplicationInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgramApplication.objects.all()
    serializer_class = ProgramApplicationSerializer
