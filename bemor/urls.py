from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (
    BemorQoshishCreateView,
    ManzilListCreateView,
    OperatsiyaBolganJoyListCreateView,
)

urlpatterns = [
    path(_("bemor-qoshish/"), BemorQoshishCreateView.as_view(), name="bemor-qoshish"),
    path(_("manzil/"), ManzilListCreateView.as_view(), name="manzil-list"),
    path(_("operatsiya-bolgan-joy/"), OperatsiyaBolganJoyListCreateView.as_view(), name="operatsiya-list"),
]
