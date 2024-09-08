"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# LibraryProject/urls.py
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False), name='home'),
    path('', include('relationship_app.urls')),  # Include the URLs from relationship_app
    path('admin/', admin.site.urls),
]


"""
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

# Create an admin user
admin_user = User.objects.create_user(username='adminuser', password='adminpassword')
UserProfile.objects.create(user=admin_user, role='Admin')

# Create a librarian user
librarian_user = User.objects.create_user(username='librarianuser', password='librarianpassword')
UserProfile.objects.create(user=librarian_user, role='Librarian')

# Create a member user
member_user = User.objects.create_user(username='memberuser', password='memberpassword')
UserProfile.objects.create(user=member_user, role='Member')

# Verify the roles
print("Admin User:", admin_user.username, admin_user.userprofile.role)
print("Librarian User:", librarian_user.username, librarian_user.userprofile.role)
print("Member User:", member_user.username, member_user.userprofile.role)

"""