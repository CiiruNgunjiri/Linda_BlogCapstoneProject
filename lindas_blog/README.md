# Lindas Blog

Lindas Blog is a Django-based web application designed to allow users to create, manage, and interact with blog posts. The application supports user authentication, comments, likes, and categorization of posts.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Templates](#templates)

## Features

- User registration and authentication using JWT.
- Create, read, update, and delete blog posts.
- Categorize posts with tags.
- Comment on posts.
- Like posts.
- User profiles with optional profile pictures.

## Technologies Used

- **Django**: Web framework for building the application.
- **Django REST Framework**: For building the API.
- **Markdown2**: For converting Markdown content to HTML.
- **SQLite**: Default database for development (consider using PostgreSQL in production).
- **HTML/CSS**: For front-end templates and styling.
- **JavaScript**: For interactive elements (if applicable).

## Project Structure

lindas_blog/
├── Procfile
├── blog/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations/
│ ├── models.py
│ ├── serializers.py
│ ├── templates/
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── db.sqlite3
├── gitignore
├── lindas_blog/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
└── staticfiles/

## Setup Instructions

1. **Clone the Repository**:

git clone https://github.com/CiiruNgunjiri/Linda_BlogCapstoneProject.git

2. **Create a Virtual Environment**:

python -m venv venv # Create a virtual environment named 'venv'
source venv/bin/activate # Activate the virtual environment (Linux/Mac)
.\venv\Scripts\activate # Activate the virtual environment (Windows)

3. **Install Dependencies**:

pip install -r requirements.txt # Install required packages

4. **Set Up Environment Variables**:
Create a `.env` file in the root directory and add your secret keys and database URL:

SECRET_KEY=m81ig)tprk+hh=+$+wd$bh#fp^7mn3kjz$9r*yxscfxh8ig4!f

DATABASE_URL=postgres://u37pd5ec92182v:p065fd94ef6c2f0d76bc9e95fdbbc951aa16bc7758ce06fd8c28e46c1c55c2490@ec2-54-208-211-87.compute-1.amazonaws.com:5432/dbge8nq6a1estr # or your database URL for production

DEBUG=True # Set to False in production

5. **Run Migrations**:

python manage.py migrate # Apply migrations to set up the database schema

6. **Create a Superuser** (optional):

python manage.py createsuperuser # Create an admin user to access the admin panel

7. **Run the Development Server**:

python manage.py runserver # Start the development server at http://127.0.0.1:8000/

## Usage

You can access the application by navigating to `http://127.0.0.1:8000/` in your web browser. Use the admin panel at `http://127.0.0.1:8000/admin/` to manage blog posts and users.

## API Endpoints

### Authentication

- `POST /api/token/`: Obtain JWT token for authentication.
- `POST /api/token/refresh/`: Refresh JWT token.

### Blog Posts

- `GET /api/posts/`: Retrieve all blog posts.
- `POST /api/posts/`: Create a new blog post.
- `GET /api/posts/<id>/`: Retrieve a specific blog post by ID.
- `PUT /api/posts/<id>/`: Update a specific blog post by ID.
- `DELETE /api/posts/<id>/`: Delete a specific blog post by ID.

### Categories

- `GET /api/categories/`: Retrieve all categories.
- `POST /api/categories/`: Create a new category.
- `GET /api/categories/<id>/`: Retrieve a specific category by ID.
- `PUT /api/categories/<id>/`: Update a specific category by ID.
- `DELETE /api/categories/<id>/`: Delete a specific category by ID.

### Comments

- `GET /api/comments/`: Retrieve all comments.
- `POST /api/comments/`: Create a new comment on a post.

### Likes

- `GET /api/likes/`: Retrieve all likes.
- `POST /api/likes/`: Like a post.

### Profiles

- `GET /api/profiles/<id>/`: Retrieve user profile by ID.
- `PUT /api/profiles/<id>/`: Update user profile by ID.

## Templates

The application includes HTML templates for rendering web pages if you choose to serve content directly rather than just providing an API.
