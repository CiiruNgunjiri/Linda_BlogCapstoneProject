from django.urls import path
from .views import PostList, PostDetail, CategoryList, CategoryDetail, CommentList, CommentDetail, LikeList, LikeDetail, ProfileDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Blog post URLs
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    # Category URLs
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    
    # Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Comment URLs
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    
    # Like URLs
    path('likes/', LikeList.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),
    
    # User profile URLs
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]

