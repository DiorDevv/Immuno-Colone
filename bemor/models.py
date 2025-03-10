from django.db import models

from shared.models import BaseModel


class Manzil(BaseModel):
    mamlakat = models.CharField(max_length=255)
    hudud = models.CharField(max_length=255)
    tuman = models.CharField(max_length=255)
    mahalla = models.CharField(max_length=255)
    kocha_nomi = models.CharField(max_length=50)
    biriktirilgan_tuman = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Manzil"
        verbose_name_plural = "Manzillar"

    def __str__(self):
        return self.mamlakat


class OperatsiyaBolganJoy(BaseModel):
    mamlakat = models.CharField(max_length=255)
    operatsiya_bolgan_joy = models.CharField(max_length=255)
    transplantatsiya_sana = models.DateField()
    operatsiya_oxirlangan_sana = models.DateField()
    ishlatilgan_miqdor = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Operatsiya joyi"
        verbose_name_plural = "Operatsiya joylari"

    def __str__(self):
        return self.mamlakat


class Jinsi(BaseModel):
    GENDER_CHOICES = [
        ('M', 'Erkak'),
        ('F', 'Ayol')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = "Jinsi"
        verbose_name_plural = "Jinslar"

    def __str__(self):
        return self.gender


class BemorningHolati(BaseModel):
    holati = models.CharField(max_length=255)
    ozgarish = models.TextField()

    class Meta:
        verbose_name = "Bemor holati"
        verbose_name_plural = "Bemorlar holati"

    def __str__(self):
        return self.holati


class Bemor(BaseModel):
    JSHSHIR = models.CharField(max_length=30)
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    tugilgan_sana = models.DateField()
    jinsi = models.ForeignKey(Jinsi, on_delete=models.CASCADE)
    manzil = models.ForeignKey(Manzil, on_delete=models.SET_NULL, null=True, blank=True)
    bemor_holati = models.ForeignKey(BemorningHolati, on_delete=models.CASCADE, null=True, blank=True)
    operatsiya_bolgan_joy = models.ForeignKey(OperatsiyaBolganJoy, on_delete=models.CASCADE, null=True, blank=True)
    biriktirilgan_file = models.FileField(upload_to='biriktirilgan/%Y/%m/%d', null=True, blank=True)
    qoshimcha_malumotlar = models.TextField(null=True, blank=True)
    # biriktirilgan_shiforkot = models.ForeignKey(SHifokor, blank=True, null=True)
    arxivga_olingan_sana = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Bemor"
        verbose_name_plural = "Bemorlar"
        constraints = [
            models.UniqueConstraint(fields=['ism', 'familiya', 'tugilgan_sana'], name='unique_bemor')
        ]

    def __str__(self):
        return f"Bemornig ismi {self.ism}, Familiya {self.familiya}"

    def sharifi(self):
        return f"Bemornig sharifi {self.ism} {self.familiya}"
