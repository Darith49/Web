from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.accounts.urls')),  # Important: crm.accounts.urls
    path('ckeditor/', include('ckeditor_uploader.urls')),
]