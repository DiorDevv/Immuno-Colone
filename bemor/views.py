from rest_framework import status, generics, serializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.translation import gettext_lazy as _
from .models import BemorQoshish, Manzil, OperatsiyaBolganJoy
from .serializers import BemorQoshishSerializer, ManzilSerializer, OperatsiyaBolganJoySerializer


class BemorQoshishCreateView(CreateAPIView):
    queryset = BemorQoshish.objects.all()
    serializer_class = BemorQoshishSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            bemor_data = serializer.validated_data

            bemor, created = BemorQoshish.objects.get_or_create(
                JSHSHIR=bemor_data["JSHSHIR"],
                defaults=bemor_data
            )

            return Response(
                {
                    "message": _("Bemor muvaffaqiyatli qo‘shildi!") if created else _("Bemor allaqachon mavjud!"),
                    "data": {
                        "JSHSHIR": bemor.JSHSHIR,
                        "ism": bemor.ism,
                        "familiya": bemor.familiya,
                        "tugilgan_sana": bemor.tugilgan_sana,
                        "jinsi": bemor.jinsi,
                    }
                },
                status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
            )

        return Response(
            {
                "message": _("Xatolik yuz berdi!"),
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class ManzilListCreateView(generics.ListCreateAPIView):
    queryset = Manzil.objects.all()
    serializer_class = ManzilSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        mamlakat = data.get("mamlakat")
        hudud = data.get("hudud")

        existing_manzil = Manzil.objects.filter(mamlakat=mamlakat, hudud=hudud).first()
        if existing_manzil:
            return Response(
                {"message": _("Bu manzil allaqachon mavjud!"), "data": ManzilSerializer(existing_manzil).data},
                status=status.HTTP_200_OK
            )

        return super().create(request, *args, **kwargs)


class OperatsiyaBolganJoyListCreateView(generics.ListCreateAPIView):
    queryset = OperatsiyaBolganJoy.objects.all()
    serializer_class = OperatsiyaBolganJoySerializer
    permission_classes = [AllowAny]
