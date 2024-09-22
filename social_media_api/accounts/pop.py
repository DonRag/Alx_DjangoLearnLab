from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

# Data for Wick family users
wick_users = [
    {'username': 'jake_wick', 'email': 'jake_wick@token.com'},
    {'username': 'jane_wick', 'email': 'jane_wick@token.com'},
    {'username': 'jimmy_wick', 'email': 'jimmy_wick@token.com'},
    {'username': 'joey_wick', 'email': 'joey_wick@token.com'},
    {'username': 'julie_wick', 'email': 'julie_wick@token.com'},
]

# Data for posts (will belong to the users created above)
wick_posts = [
    {'title': 'The Art of Stealth', 'content': 'Mastering stealth is essential in every mission.', 'author': 'johnwick'},
    {'title': 'Target Practice', 'content': 'Hitting bullseye from a mile away.', 'author': 'jane_wick'},
    {'title': 'Escape Routes', 'content': 'Always plan two exit strategies.', 'author': 'jimmy_wick'},
    {'title': 'Weapons Training', 'content': 'Different weapons for different tasks.', 'author': 'joey_wick'},
    {'title': 'Undercover Operations', 'content': 'Blend in and adapt to every environment.', 'author': 'julie_wick'},
]

# Data for comments (on posts)
wick_comments = [
    {'post_title': 'The Art of Stealth', 'content': 'Invaluable advice! Thanks for sharing.', 'author': 'jane_wick'},
    {'post_title': 'Target Practice', 'content': 'I need to improve my range skills.', 'author': 'jimmy_wick'},
    {'post_title': 'Escape Routes', 'content': 'Always plan a third exit route too!', 'author': 'jake_wick'},
    {'post_title': 'Weapons Training', 'content': 'Agreed, preparation is key.', 'author': 'julie_wick'},
    {'post_title': 'Undercover Operations', 'content': 'Blending in is a skill on its own.', 'author': 'joey_wick'},
]

# Create Wick family users
for user_data in wick_users:
    try:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={'email': user_data['email']}
        )
        if created:
            user.set_password('token2030')
            user.save()
            print(f"User {user_data['username']} created.")
        else:
            print(f"User {user_data['username']} already exists.")
    except Exception as e:
        print(f"Error creating user {user_data['username']}: {e}")

# Create posts by Wick family users
for post_data in wick_posts:
    try:
        user = User.objects.get(username=post_data['author'])
        post, created = Post.objects.get_or_create(
            title=post_data['title'],
            author=user,
            defaults={'content': post_data['content']}
        )
        if created:
            print(f"Post '{post_data['title']}' created by {post_data['author']}.")
        else:
            print(f"Post '{post_data['title']}' by {post_data['author']} already exists.")
    except ObjectDoesNotExist:
        print(f"Author {post_data['author']} does not exist.")
    except Exception as e:
        print(f"Error creating post {post_data['title']}: {e}")

# Create comments on posts by Wick family users
for comment_data in wick_comments:
    try:
        post = Post.objects.get(title=comment_data['post_title'])
        user = User.objects.get(username=comment_data['author'])
        comment, created = Comment.objects.get_or_create(
            post=post,
            author=user,
            defaults={'content': comment_data['content']}
        )
        if created:
            print(f"Comment by {comment_data['author']} on '{comment_data['post_title']}' created.")
        else:
            print(f"Comment by {comment_data['author']} on '{comment_data['post_title']}' already exists.")
    except ObjectDoesNotExist as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error creating comment on post '{comment_data['post_title']}': {e}")
