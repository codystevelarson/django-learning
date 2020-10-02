from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API ENDPOINT ALLOWING USERS TO BE VIEWED OR EDITED
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
        API ENDPOINT ALLOWING G TO BE VIEWED OR EDITED
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.AllowAny]