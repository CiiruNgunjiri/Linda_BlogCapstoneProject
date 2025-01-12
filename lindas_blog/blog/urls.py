from django.urls import path
from . import views  # Correct import of views
from .views import (
    PostList,
    PostDetail,
    CategoryList,
    CategoryDetail,
    CommentList,
    CommentDetail,
    LikeList,
    LikeDetail,
    ProfileDetail
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

app_name = 'blog'  # Namespace for the app

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile API endpoint (used in the profile detail view)
    path('api/profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    
    # Post API URLs
    path('api/posts/', PostList.as_view(), name='post-list-api'),
    path('api/posts/<int:id>/', PostDetail.as_view(), name='post-detail-api'),
    
    # Category API URLs
    path('api/categories/', CategoryList.as_view(), name='category-list-api'),
    path('api/categories/<int:id>/', CategoryDetail.as_view(), name='category-detail-api'),
    
    # Blog post URLs (Frontend)
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    # Category URLs (Frontend)
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    
    # Comment URLs (Frontend)
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    
    # Like URLs (Frontend)
    path('likes/', LikeList.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),
    
    # User profile URLs (Frontend)
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]
