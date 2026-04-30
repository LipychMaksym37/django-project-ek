from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # ← ГОЛОВНЕ
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # ← ДОДАЙ ЦЕ
    path('', include('main.urls')),
]