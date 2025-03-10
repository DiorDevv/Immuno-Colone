from django.urls import path
from .views import BemorQoshishCreateView, ManzilListCreateView, OperatsiyaBolganJoyListCreateView

urlpatterns = [
    path('bemor-qoshish/', BemorQoshishCreateView.as_view(), name='bemor-qoshish'),
    path('manzil/', ManzilListCreateView.as_view(), name='manzil'),
    path('operatsiya/', OperatsiyaBolganJoyListCreateView.as_view(), name='operatsiya-list-create'),

]
