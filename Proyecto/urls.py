from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppSport/', include('AppSport.urls')),
    path('', RedirectView.as_view(url='/AppSport/', permanent=True)),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
