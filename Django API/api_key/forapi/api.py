from .models import ForAPI
from rest_framework import viewsets, permissions
from .serializers import ForAPISerializer


class ForAPIViewsSet(viewsets.ModelViewSet):
    queryset = ForAPI.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ForAPISerializer
