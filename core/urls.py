
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('store/', include('store.urls')),
    path((''), views.home, name='home'),
    # path(('store/'), views.store, name='store'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
