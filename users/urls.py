from django.urls import path

from .views import CreateUserView, LoginAPIView, #LoginRefreshView

urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("login/", LoginAPIView.as_view(), name="login"),
    # path('login/refresh/', LoginRefreshView.as_view(), name='login_refresh'),

]
