from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),  # Include the posts app URLs under the `/api/` path
    path('notifications/', include('notifications.urls')),
]
