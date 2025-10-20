from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medical/', include('medical.urls')),
    path('', include('spa_app.urls')),
]