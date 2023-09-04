# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('website/', include('website.urls')),
]
# urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)
