from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    # statics
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
