from django.urls import path
from .views import ProgramApplicationListCreate, ProgramApplicationInfo


urlpatterns = [
    path('', ProgramApplicationListCreate.as_view(), name='program_application_list_create'),
    path('api/student/<int:pk>/', ProgramApplicationInfo.as_view(), name='program_application_info'),
]