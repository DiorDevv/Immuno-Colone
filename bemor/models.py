from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel
from django.core.validators import RegexValidator

User = get_user_model()


class Manzil(BaseModel):
    mamlakat = models.CharField(_("Mamlakat"), max_length=255)
    hudud = models.CharField(_("Hudud"), max_length=255)
    tuman = models.CharField(_("Tuman"), max_length=255)
    mahalla = models.CharField(_("Mahalla"), max_length=255)
    kocha_nomi = models.CharField(_("Ko‘cha nomi"), max_length=50)
    biriktirilgan_tuman = models.CharField(_("Biriktirilgan tuman"), max_length=255)

    class Meta:
        verbose_name = _("Manzil")
        verbose_name_plural = _("Manzillar")

    def __str__(self):
        return self.mamlakat


from django.db import models
from django.utils.translation import gettext_lazy as _


class OperatsiyaBolganJoy(models.Model):
    MAMLAAKATLAR = [
        ("UZ", _("O‘zbekiston")),
        ("RU", _("Rossiya")),
        ("US", _("AQSh")),
        # Boshqa mamlakatlar...
    ]

    OPERATSIYA_TURLARI = [
        ("jigar", _("Jigar transplantatsiyasi")),
        ("yurak", _("Yurak transplantatsiyasi")),
        ("buyrak", _("Buyrak transplantatsiyasi")),
    ]

    mamlakat = models.CharField(_("Mamlakat"), max_length=255, choices=MAMLAAKATLAR)
    operatsiya_bolgan_joy = models.CharField(_("Operatsiya bo‘lgan joy"), max_length=255)
    transplantatsiya_sana = models.DateField(_("Transplantatsiya sanasi"))
    transplantatsiya_operatsiyasi = models.CharField(
        _("Transplantatsiya operatsiyasi"), max_length=255, choices=OPERATSIYA_TURLARI
    )
    operatsiya_oxirlangan_sana = models.DateField(_("Operatsiya oxirlangan sana"))
    ishlatilgan_miqdor = models.PositiveSmallIntegerField(_("Ishlatilgan miqdor"))

    class Meta:
        verbose_name = _("Operatsiya joyi")
        verbose_name_plural = _("Operatsiya joylari")

    def __str__(self):
        return f"Operatsiya bo'lgan joy {self.operatsiya_bolgan_joy}"


class BemorningHolati(BaseModel):
    holati = models.CharField(_("Holati"), max_length=255)
    ozgarish = models.TextField(_("O‘zgarish"))

    class Meta:
        verbose_name = _("Bemor holati")
        verbose_name_plural = _("Bemorlar holati")

    def __str__(self):
        return self.holati


class BemorQoshish(models.Model):
    GENDER_CHOICES = [
        ('M', _("Erkak")),
        ('F', _("Ayol")),
    ]

    JSHSHIR = models.CharField(
        _("JSHSHIR"),
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{14}$',
                message=_("JSHSHIR faqat 14 ta raqamdan iborat bo‘lishi kerak!")
            )
        ]
    )
    ism = models.CharField(_("Ism"), max_length=255)
    familiya = models.CharField(_("Familiya"), max_length=255)
    tugilgan_sana = models.DateField(_("Tug‘ilgan sana"))
    jinsi = models.CharField(_("Jinsi"), max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = _("Bemor JSHSHIR")
        verbose_name_plural = _("Bemor JSHSHIRlar")
        constraints = [
            models.UniqueConstraint(fields=['ism', 'familiya', 'tugilgan_sana'], name='unique_bemor')
        ]

    def __str__(self):
        return f"{self.ism} {self.familiya} - {self.JSHSHIR}"


class Bemor(BaseModel):
    bemor = models.ForeignKey(BemorQoshish, verbose_name=_("Bemor"), on_delete=models.CASCADE)
    manzil = models.ForeignKey(Manzil, verbose_name=_("Manzil"), on_delete=models.SET_NULL, null=True, blank=True)
    bemor_holati = models.ForeignKey(BemorningHolati, verbose_name=_("Bemor holati"), on_delete=models.CASCADE,
                                     null=True, blank=True)
    operatsiya_bolgan_joy = models.ForeignKey(OperatsiyaBolganJoy, verbose_name=_("Operatsiya bo‘lgan joy"),
                                              on_delete=models.CASCADE, null=True, blank=True)
    biriktirilgan_file = models.FileField(_("Biriktirilgan fayl"), upload_to='media/biriktirilgan/%Y/%m/%d', null=True,
                                          blank=True)
    qoshimcha_malumotlar = models.TextField(_("Qo‘shimcha ma'lumotlar"), null=True, blank=True)
    arxivga_olingan_sana = models.DateTimeField(_("Arxivga olingan sana"), null=True, blank=True)

    class Meta:
        verbose_name = _("Bemor")
        verbose_name_plural = _("Bemorlar")

    def __str__(self):
        return f"{self.bemor.ism} {self.bemor.familiya} - {self.bemor.JSHSHIR}"
