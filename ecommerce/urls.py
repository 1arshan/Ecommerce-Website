from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'), name='app_store'),
    path('', include('accounts.urls'), name='auth'),
    path('', include('store.api.urls'), name='api'),
    path('', include('django.contrib.auth.urls')),
    # path('', include('django.contrib.auth.urls')),
    # path(r'^oauth/', include('social_django.urls', namespace='social')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
