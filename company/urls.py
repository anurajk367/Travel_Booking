
from django.contrib import admin
from django.urls import path,include
from account.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/',include("account.urls")),
    path('', Logview.as_view(),name='log'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


