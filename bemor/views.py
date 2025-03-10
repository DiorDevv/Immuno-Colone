from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Jinsi
from .serializers import JinsiSerializer


class JinsiCreateView(CreateAPIView):
    queryset = Jinsi.objects.all()
    serializer_class = JinsiSerializer

    def perform_create(self, serializer):
        jinsi = serializer.save()
        self.response_data = {
            "message": "Jins muvaffaqiyatli yaratildi!",
            "data": JinsiSerializer(jinsi).data
        }

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(self.response_data, status=status.HTTP_201_CREATED)
