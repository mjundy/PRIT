from CatatPRApp import serializers
from CatatPRApp.models import PR
from CatatPRApp.serializers import PRSerializer
from rest_framework import viewsets

class PRViewSet(viewsets.ModelViewSet):
    queryset = PR.objects.all()
    serializer_class = PRSerializer