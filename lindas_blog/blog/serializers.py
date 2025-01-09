from rest_framework import serializers
from .models import Post, Category, Tag, Comment, Like, Profile
import markdown2

class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""
    content_markdown = serializers.SerializerMethodField()  # field name

    class Meta:
        model = Post
        fields = '__all__'  # Consider specifying fields explicitly for better control

    def get_content_markdown(self, obj):
        """Convert post content from Markdown to HTML."""
        return markdown2.markdown(obj.content)  # Convert content to HTML using markdown2


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model."""
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the Tag model."""
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""
    author = serializers.ReadOnlyField(source='author.username')  # Display username of the author

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model."""
    user = serializers.ReadOnlyField(source='user.username')  # Display username of the user who liked

    class Meta:
        model = Like
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model."""
    user = serializers.ReadOnlyField(source='user.username')  # Display username associated with the profile

    class Meta:
        model = Profile
        fields = '__all__'
