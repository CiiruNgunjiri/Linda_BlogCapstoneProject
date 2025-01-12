from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Post, Category, Comment, User, Profile
from .serializers import PostSerializer
from rest_framework.test import APIClient

class BlogTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        """Set up test data and environment."""
        # Create user for testing (if not already exists)
        self.user, created = User.objects.get_or_create(username="testuser", email="test@example.com")
        self.client.force_authenticate(user=self.user)

        # Ensure no profile exists and create a fresh one for the user
        Profile.objects.filter(user=self.user).delete()
        self.profile = Profile.objects.create(user=self.user, bio="This is a test bio")

        # Create a category for posts
        self.category = Category.objects.create(name="Tech")

        # Create a post for testing
        self.post = Post.objects.create(
            title="Test Post", 
            content="This is a test post.", 
            author=self.user, 
            category=self.category,
            is_draft=False
        )

        # Initialize the API client for testing
        self.api_client = APIClient()

    # 1. Test HTML Views
    
    def test_home_page(self):
        """Test the home page renders correctly."""
        response = self.client.get(reverse('blog:post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')  # Ensure the correct template is used
        if response.status_code == 301:
            print('Redirect location:', response['Location'])
            
    def test_post_detail_page(self):
        """Test that the post detail page renders correctly."""
        response = self.client.get(reverse('blog:post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_category_page(self):
        """Test the category list page."""
        response = self.client.get(reverse('blog:category-list'))
        self.assertEqual(response.status_code, 200)

    # 2. Test API Views

    def test_get_posts_api(self):
        """Test the GET request for the post API."""
        response = self.api_client.get(reverse('blog:post-list-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_api(self):
        """Test creating a new post via the API."""
        self.api_client.force_authenticate(user=self.user)  # Authenticate with the test user
        data = {
            "title": "New Post",
            "content": "This is a new post.",
            "category": self.category.id,
            "author": self.user.id,
            "is_draft": False
        }
        response = self.api_client.post(reverse('blog:post-list-api'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_detail_api(self):
        """Test the GET request for the post detail API."""
        response = self.api_client.get(reverse('blog:post-detail-api', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post_api(self):
        """Test deleting a post via the API."""
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.delete(reverse('blog:post-detail-api', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_like_post_api(self):
        """Test liking a post via the API."""
        self.api_client.force_authenticate(user=self.user)
        data = {
            "post": self.post.id,
        }
        response = self.api_client.post(reverse('blog:like-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 3. Test Serializers

    def test_post_serializer(self):
        """Test the Post serializer."""
        data = {
            'id': self.post.id,
            'title': self.post.title,
            'content': self.post.content,
            'content_html': '<p>This is a test post</p>',  # Example HTML output from Markdown
            'author': self.post.author.username,
            'slug': self.post.slug,
            'category': self.post.category.name,
            'published_date': self.post.published_date,
            'created_date': self.post.created_date,
            'tags': [tag.name for tag in self.post.tags.all()],
            'is_draft': self.post.is_draft,
        }
        serializer = PostSerializer(self.post)
        self.assertEqual(serializer.data, data)

    # 4. Test Model Methods and Properties
    import uuid

def test_post_markdown_conversion(self):
    """Test the Markdown conversion in Post."""
    # Create a unique title to avoid slug collisions
    unique_title = "Test Markdown Post - " + str(uuid.uuid4())
    
    # Create the post with a unique slug generated from the title
    post = Post.objects.create(
        title=unique_title,  # Use the unique title
        content="**Bold Text**", 
        author=self.user, 
        category=self.category
    )
    
    # Check if the markdown was converted to HTML correctly
    self.assertIn('<strong>Bold Text</strong>', post.content_html)  # Check if Markdown was converted

    def test_profile_creation(self):
        """Test profile creation."""
        profile = Profile.objects.create(user=self.user, bio="Test Bio")
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, "Test Bio")
