# Social Media API

This project is a Django-based social media API that includes functionalities for user registration, authentication, creating and managing posts and comments, following/unfollowing users, generating a personalized user feed, and implementing notifications and likes functionality.

## Table of Contents
- [Task 0: Setup](#task-0-setup)
- [Task 1: Posts and Comments API](#task-1-posts-and-comments-api)
  - [Posts Endpoint](#posts-endpoint)
  - [Comments Endpoint](#comments-endpoint)
- [Task 2: Follow & Feed API](#task-2-follow--feed-api)
  - [Follow a User](#follow-a-user)
  - [Unfollow a User](#unfollow-a-user)
  - [User Feed](#user-feed)
- [Task 3: Notifications and Likes API](#task-3-notifications-and-likes-api)
  - [Like a Post](#like-a-post)
  - [Unlike a Post](#unlike-a-post)
  - [View Notifications](#view-notifications)
- [Project Setup](#project-setup)

---

## Task 0: Setup

(Setup instructions from Task 0 remain unchanged)

---

## Task 1: Posts and Comments API

(Documentation for Task 1 remains unchanged)

---

## Task 2: Follow & Feed API

(Documentation for Task 2 remains unchanged)

---

## Task 3: Notifications and Likes API

### Like a Post

- **Endpoint**: `/api/posts/<int:pk>/like/`
- **Method**: `POST`
- **Description**: Allows the current authenticated user to like a post.
- **Permissions**: Only authenticated users can like posts.

#### Request Example
```bash
POST /api/posts/1/like/
Authorization: Token <your_token>
```

#### Response Example (Success)
```json
{
  "message": "Post liked successfully"
}
```

#### Response Example (Already Liked)
```json
{
  "error": "You have already liked this post"
}
```

### Unlike a Post

- **Endpoint**: `/api/posts/<int:pk>/unlike/`
- **Method**: `POST`
- **Description**: Allows the current authenticated user to unlike a post they have previously liked.
- **Permissions**: Only authenticated users can unlike posts.

#### Request Example
```bash
POST /api/posts/1/unlike/
Authorization: Token <your_token>
```

#### Response Example (Success)
```json
{
  "message": "Post unliked successfully"
}
```

#### Response Example (Not Liked Yet)
```json
{
  "error": "You have not liked this post yet"
}
```

### View Notifications

- **Endpoint**: `/api/notifications/`
- **Method**: `GET`
- **Description**: Allows the current authenticated user to view their notifications, showing unread notifications prominently.
- **Permissions**: Only authenticated users can view notifications.

#### Request Example
```bash
GET /api/notifications/
Authorization: Token <your_token>
```

#### Response Example (Unread Notifications)
```json
[
  {
    "id": 1,
    "recipient": "john_doe",
    "actor": "jane_doe",
    "verb": "liked your post",
    "target": "Post 1",
    "timestamp": "2024-09-22T10:00:00Z",
    "read": false
  }
]
```

#### Response Example (Read Notifications)
```json
[
  {
    "id": 2,
    "recipient": "john_doe",
    "actor": "jane_doe",
    "verb": "started following you",
    "target": null,
    "timestamp": "2024-09-22T09:45:00Z",
    "read": true
  }
]
```

### Notification Triggers
Notifications are generated for the following actions:
- A user likes your post.
- A user comments on your post.
- A user starts following you.

---


## Task 4: Deploying the Django REST API to Production

### Objective
The objective of this task is to deploy the **social_media_api** Django REST API project to a production environment, making it accessible for real-world testing and interaction.

### Deployment Overview

The deployment process involves the following steps:

1. **Prepare the Project for Production**
   - Modify settings for production.
   - Ensure security configurations are in place.

2. **Choose a Hosting Service**
   - Select and set up a cloud hosting provider (Heroku, DigitalOcean, or AWS).

3. **Set Up a Web Server and WSGI**
   - Use Gunicorn as the application server.
   - Configure Nginx (for DigitalOcean) as a reverse proxy.

4. **Manage Static Files and Databases**
   - Handle static and media files, and ensure proper database configuration.

5. **Deploy the Application**
   - Push the code to a repository and deploy using the chosen hosting service.

6. **Monitor and Maintain the Application**
   - Set up monitoring for the application’s performance and health.

7. **Documentation and Final Testing**
   - Ensure the application is fully functional and provide complete documentation.

### Step 1: Prepare the Project for Production

#### Production Settings (`settings.py`)

Make the following changes in your `settings.py` file:

```python
DEBUG = False
ALLOWED_HOSTS = ['your_domain_or_ip', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True
```

If AWS S3 is used for static/media files:

```python
if os.getenv('USE_AWS') == 'TRUE':
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'
```

### Step 2: Choose a Hosting Service

#### Hosting Selection

The project can be hosted on Heroku, AWS, or DigitalOcean. Below is a summary of the steps taken for **Heroku** and **DigitalOcean** deployment:

#### **Heroku Deployment**:
1. Install the Heroku CLI and log in using `heroku login`.
2. Create a Heroku app with `heroku create your-app-name`.
3. Add the `ClearDB` MySQL add-on to manage the database.
4. Push the project to Heroku using Git:
   ```bash
   git push heroku main
   ```

#### **DigitalOcean Deployment**:
1. Create a Django One-Click Droplet.
2. Set up Nginx and Gunicorn on the server.
3. Configure MySQL or use an external database like AWS RDS.

### Step 3: Set Up a Web Server and WSGI

#### **Gunicorn Setup**
Install and configure Gunicorn to run the Django app:

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```
2. Add a `Procfile` to the project root:
   ```
   web: gunicorn social_media_api.wsgi --log-file -
   ```

#### **Nginx Setup (For DigitalOcean)**

Set up Nginx as a reverse proxy:

```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/static/files;
    }

    location /media/ {
        alias /path/to/media/files;
    }
}
```

### Step 4: Manage Static Files and Databases

1. **Static and Media Files**:
   - Collect static files using:
     ```bash
     python manage.py collectstatic
     ```
   - Configure AWS S3 if used for static and media file storage.

2. **Database Configuration**:
   - The MySQL database is configured using environment variables. For Heroku, the `ClearDB` add-on was used to set up MySQL.

### Step 5: Deploy the Application

1. Push the project to a Git repository like GitHub:
   ```bash
   git push origin main
   ```
2. Deploy to Heroku:
   ```bash
   git push heroku main
   ```
3. For DigitalOcean, follow the guide for manually deploying the app on a droplet.

### Step 6: Monitor and Maintain the Application

1. **Monitoring**:
   -

 Use services like Sentry for error tracking.
   - Utilize logging and monitoring tools to keep an eye on performance.

2. **Maintenance**:
   - Regularly update dependencies and monitor server health.

### Step 7: Documentation and Final Testing

1. Ensure that all API endpoints are functioning as expected.
2. Document any environment variables and setup steps for future reference.

---

## Project Setup

(Setup instructions remain unchanged)
