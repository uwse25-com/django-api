from rest_framework import status, viewsets
from rest_framework.views import Response
from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
