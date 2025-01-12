from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Post, Category, Comment, Like, Profile
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer, ProfileSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Custom error handlers
def handler404(request, exception):
    """Custom 404 error handler."""
    return render(request, '404.html', status=404)

def handler500(request):
    """Custom 500 error handler."""
    return render(request, '500.html', status=500)

# Post Detail View for rendering HTML
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Fetch the post by ID
    return render(request, 'blog/post_detail.html', {'post': post})

# Category List View (optional)
def category_list(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'blog/category_list.html', {'categories': categories})


class PublishedPostList(generics.ListAPIView):
    """API view to retrieve only published blog posts."""
    queryset = Post.objects.published()  # Use the custom manager method
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view published posts


class UserRegister(generics.CreateAPIView):
    """API view for user registration."""
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            raise ValidationError("All fields are required.")

        user = User(username=username, email=email)
        user.set_password(password)  # Hash the password
        user.save()

        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)


class PostList(generics.ListCreateAPIView):
    """API view to retrieve and create blog posts."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        
        """Optionally filter posts by draft status."""
        queryset = super().get_queryset()
        is_draft = self.request.query_params.get('is_draft', None)
        
        if is_draft is not None:
            queryset = queryset.filter(is_draft=is_draft.lower() == 'true')
        
        return queryset
        
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete a specific blog post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_update(self, serializer):
        """Ensure that only the author can update their post."""
        serializer.save(author=self.request.user)


class CategoryList(generics.ListCreateAPIView):
    """API view to retrieve and create categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete a specific category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentList(generics.ListCreateAPIView):
    """API view to retrieve and create comments on posts."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Set the author of the comment to the current user."""
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update, or delete a specific comment."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeList(generics.ListCreateAPIView):
    """API view to retrieve and create likes for posts."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Ensure that a user can like a post only once."""
        post_id = self.request.data.get('post')

        if Like.objects.filter(post_id=post_id, user=self.request.user).exists():
            raise ValidationError("You have already liked this post.")
        
        serializer.save(user=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """API view to retrieve or delete a specific like."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """API view to retrieve or update a user's profile."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

