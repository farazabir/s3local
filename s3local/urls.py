from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s3/', include('core.urls')),
        path('', lambda r: JsonResponse({"status": "ok"}))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)