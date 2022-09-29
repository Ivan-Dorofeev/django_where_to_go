from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from where_to_go import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('places/', include('places.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
