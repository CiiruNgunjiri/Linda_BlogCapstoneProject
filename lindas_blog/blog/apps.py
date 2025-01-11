from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Configuration for the Blog application."""
    
    default_auto_field = 'django.db.models.BigAutoField'  # Use BigAutoField as the default primary key field type
    name = 'blog'  # The name of the application
    verbose_name = "Blog Application"  # Human-readable name for the application

    def ready(self):
        """Override this method to perform startup actions."""
        # Import signals or perform any startup tasks here
        pass
