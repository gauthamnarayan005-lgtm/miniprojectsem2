# workshopmanagement/workshop_main/workshop_main/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Import the home view directly to map it to the root
from accounts.views import home_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Map the root URL directly to the home view
    path('', home_view, name='home'), 
    path('services/', include('services.urls', namespace='services')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

# This part is causing the "Directory indexes are not allowed" error 
# because it is trying to serve media at the root path when no other URL matches.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)