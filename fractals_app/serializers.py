from django.contrib.auth.models import User
from rest_framework import serializers

from fractals_app.models import Fractal


class FractalSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Fractal
        fields = ["id", "created", "creator", "name"]


class UserSerializer(serializers.ModelSerializer):
    fractals = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Fractal.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "fractals"]
