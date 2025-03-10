from django.urls import path
from .views import JinsiCreateView

urlpatterns = [
    path('jinslar/create/', JinsiCreateView.as_view(), name='jinsi-create'),
]
