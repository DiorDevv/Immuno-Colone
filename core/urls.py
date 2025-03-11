from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin paneli i18n bilan o‘ralmaydi
]

urlpatterns += i18n_patterns(
    path("users/api/", include("users.urls")),
        path("bemor/api/", include("bemor.urls")),
)
