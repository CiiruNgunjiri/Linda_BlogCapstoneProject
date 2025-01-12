from django.contrib import admin
from django.urls import path, include
from blog.views import handler404, handler500

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include blog app URLs for both frontend and API
    path('api/', include('blog.urls')),  # API URLs are now included from blog/urls.py

    # Optional: Custom error handling views can be added here if needed
]

# Custom error handling views
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
