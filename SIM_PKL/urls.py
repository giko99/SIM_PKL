from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('catatan/', include('catatan.urls')),
    path('accounts/', include('accounts.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('mitra/', include('mitra.urls')),
    path('admin/', admin.site.urls),
]
