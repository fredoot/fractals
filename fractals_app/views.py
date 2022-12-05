from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from fractals_app.models import Fractal
from fractals_app.permissions import IsCreatorOrReadOnly
from fractals_app.serializers import FractalSerializer, UserSerializer


class FractalViewSet(viewsets.ModelViewSet):

    queryset = Fractal.objects.all()
    serializer_class = FractalSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsCreatorOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
