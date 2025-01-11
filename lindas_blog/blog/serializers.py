from rest_framework import serializers
from .models import Post, Category, Tag, Comment, Like, Profile
import markdown2

class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""
    content_html = serializers.SerializerMethodField()  # Renamed for clarity

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'content_html', 'author', 'slug', 'category', 'published_date', 'created_date', 'tags', 'is_draft']  # Explicitly specify fields

    def get_content_html(self, obj):
        """Convert post content from Markdown to HTML."""
        return markdown2.markdown(obj.content)  # Convert content to HTML using markdown2


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model."""
    
    class Meta:
        model = Category
        fields = ['id', 'name']  # Explicitly specify fields


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the Tag model."""
    
    class Meta:
        model = Tag
        fields = ['id', 'name']  # Explicitly specify fields


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""
    author = serializers.ReadOnlyField(source='author.username')  # Display username of the author

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_date']  # Explicitly specify fields


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model."""
    user = serializers.ReadOnlyField(source='user.username')  # Display username of the user who liked

    class Meta:
        model = Like
        fields = ['id', 'post', 'user']  # Explicitly specify fields


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model."""
    user = serializers.ReadOnlyField(source='user.username')  # Display username associated with the profile

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'profile_picture']  # Explicitly specify fields
