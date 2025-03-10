from rest_framework import serializers
from .models import BemorQoshish, Manzil, OperatsiyaBolganJoy


class BemorQoshishSerializer(serializers.ModelSerializer):
    class Meta:
        model = BemorQoshish
        fields = ['JSHSHIR', 'ism', 'familiya', 'tugilgan_sana', 'jinsi']

    def validate_JSHSHIR(self, value):
        if not value.isdigit() or len(value) != 14:
            raise serializers.ValidationError("JSHSHIR faqat 14 ta raqamdan iborat bo‘lishi kerak!")

        return value

    def validate(self, attrs):
        JSHSHIR = attrs.get("JSHSHIR")
        ism = attrs.get("ism")
        familiya = attrs.get("familiya")
        tugilgan_sana = attrs.get("tugilgan_sana")

        bemor = BemorQoshish.objects.filter(JSHSHIR=JSHSHIR).first()
        if bemor:
            return {
                "JSHSHIR": bemor.JSHSHIR,
                "ism": bemor.ism,
                "familiya": bemor.familiya,
                "tugilgan_sana": bemor.tugilgan_sana,
                "jinsi": bemor.jinsi,
            }

        if BemorQoshish.objects.filter(ism=ism, familiya=familiya, tugilgan_sana=tugilgan_sana).exists():
            raise serializers.ValidationError(
                {"detail": "Bunday ism, familiya va tug‘ilgan sanaga ega bemor allaqachon mavjud!"}
            )

        return attrs


class ManzilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzil
        fields = "__all__"  # Barcha maydonlarni qo‘shish

    def validate_mamlakat(self, value):
        if not value.strip():
            raise serializers.ValidationError("Mamlakat nomi bo‘sh bo‘lishi mumkin emas!")
        return value

    def validate_hudud(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Hudud nomi kamida 3 ta harfdan iborat bo‘lishi kerak!")
        return value


class OperatsiyaBolganJoySerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatsiyaBolganJoy
        fields = '__all__'

    def validate_transplantatsiya_sana(self, value):
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("Transplantatsiya sanasi kelajakda bo'lishi mumkin emas.")
        return value

    def validate_ishlatilgan_miqdor(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ishlatilgan miqdor 0 dan katta bo‘lishi kerak.")
        return value
