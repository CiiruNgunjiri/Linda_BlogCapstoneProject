from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Model to represent blog categories."""
    name = models.CharField(max_length=100, unique=True)  # Ensure category names are unique

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Model to represent tags for blog posts."""
    name = models.CharField(max_length=100, unique=True)  # Ensure tag names are unique

    def __str__(self):
        return self.name


class Post(models.Model):
    """Model to represent blog posts."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Related name for easier access
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')  # Related name for easier access
    published_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')  # Related name for easier access
    is_draft = models.BooleanField(default=True)  # Field to manage draft status

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Model to represent comments on blog posts."""
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Related name for easier access
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


class Like(models.Model):
    """Model to represent likes on blog posts."""
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')  # Ensure a user can like a post only once

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'


class Profile(models.Model):
    """Model to represent user profiles."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


def create_user_profile(sender, instance, created, **kwargs):
    """Create a user profile when a new User instance is created."""
    if created:
        Profile.objects.create(user=instance)

# Connect the signal to create a profile when a user is created
models.signals.post_save.connect(create_user_profile, sender=User)
