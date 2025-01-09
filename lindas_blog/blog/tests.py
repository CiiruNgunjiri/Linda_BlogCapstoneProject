# blog/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Post, Category

class PostAPITests(APITestCase):

    def setUp(self):
        """Create a user and a category for testing."""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')

    def test_create_post(self):
        """Test creating a new post."""
        self.client.login(username='testuser', password='testpass')
        url = reverse('post-list')
        data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'author': self.user.id,
            'category': self.category.id,
            'is_draft': False,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_list_posts(self):
        """Test listing posts."""
        Post.objects.create(title='Post 1', content='Content 1', author=self.user, category=self.category)
        Post.objects.create(title='Post 2', content='Content 2', author=self.user, category=self.category)

        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Expecting two posts

    def test_update_post(self):
        """Test updating an existing post."""
        post = Post.objects.create(title='Old Title', content='Old Content', author=self.user, category=self.category)
        self.client.login(username='testuser', password='testpass')
        
        url = reverse('post-detail', args=[post.id])
        data = {'title': 'New Title'}
        
        response = self.client.put(url, data)
        post.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.title, 'New Title')

    def test_delete_post(self):
        """Test deleting a post."""
        post = Post.objects.create(title='Post to Delete', content='Content to delete.', author=self.user, category=self.category)
        
        self.client.login(username='testuser', password='testpass')
        
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)  # Ensure the post was deleted
