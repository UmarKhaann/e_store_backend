from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # Import the "static" function
from django.conf import settings  # Import the "settings" module
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.members),
    path('', include('products.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
