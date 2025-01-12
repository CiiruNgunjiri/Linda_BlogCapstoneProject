from django.contrib import admin
from django.urls import path, include
from blog.views import handler404, handler500
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include blog app URLs for both frontend and API
    path('api/', include('blog.urls')),  # API URLs are now included from blog/urls.py

    path('login/', auth_views.LoginView.as_view(), name='login'),  # Define the 'login' view here
    # Optional: Custom error handling views can be added here if needed
]

# Custom error handling views
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
