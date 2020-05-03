from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.views.static import serve
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', obtain_auth_token),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]


