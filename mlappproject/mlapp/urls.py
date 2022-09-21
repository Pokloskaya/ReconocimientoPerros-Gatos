from django.contrib import admin
from django.urls import path
from petclassifier import views as petClassifierViews

from django.conf.urls.static import static #esto no lo decia explicitamente pero igual lo pongo
from django.conf import settings #esto no lo decia explicitamente pero igual lo pongo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', petClassifierViews.home),
    path('xception/', petClassifierViews.xception),
    path('vgg16/', petClassifierViews.vgg16),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)