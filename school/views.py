from rest_framework import viewsets
from models import Student
from serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().cache()
    serializer_class = StudentSerializer



