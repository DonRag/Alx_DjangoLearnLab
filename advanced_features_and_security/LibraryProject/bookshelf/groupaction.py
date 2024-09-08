# Import necessary modules for managing groups and permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book, CustomUser, Library

# Step 1: Define the groups and their associated permissions
# Each group is associated with specific permissions based on their roles
groups_permissions = {
    'Admins': ['can_view_book', 'can_create_book', 'can_edit_book', 'can_delete_book',
               'can_view_library', 'can_create_library', 'can_edit_library', 'can_delete_library'],
    'Editors': ['can_view_book', 'can_create_book', 'can_edit_book', 
                'can_view_library', 'can_create_library', 'can_edit_library'],
    'Viewers': ['can_view_book', 'can_view_library']
}

# Step 2: Create groups and assign permissions to them
# Loop through each group defined in the groups_permissions dictionary
for group_name, permissions in groups_permissions.items():
    # Create the group or retrieve it if it already exists
    group, created = Group.objects.get_or_create(name=group_name)
    
    # Assign the necessary permissions to the group based on the permissions list
    for perm in permissions:
        # Split the permission name to determine the model and action
        model_name = perm.split('_')[2]  # Extract model name ('book' or 'library')
        
        # Get the ContentType object for the model
        content_type = ContentType.objects.get(model=model_name)
        
        # Retrieve the Permission object by codename and content type
        permission = Permission.objects.get(codename=perm, content_type=content_type)
        
        # Add the permission to the group
        group.permissions.add(permission)

    # Provide feedback on group creation
    if created:
        print(f'Created group: {group_name}')
    else:
        print(f'Group already exists: {group_name}')

    # List out the permissions that were added to the group
    for perm in permissions:
        print(f' - Added permission: {perm} to group {group_name}')

print('Group and permission setup complete.')

# Step 3: Create users if they don't exist and assign them to groups
# Define users to be created
# users_data = [
#     {'email': 'user1@example.com', 'password': 'password1', 'first_name': 'User', 'last_name': 'One'},
#     {'email': 'user2@example.com', 'password': 'password2', 'first_name': 'User', 'last_name': 'Two'},
#     {'email': 'user3@example.com', 'password': 'password3', 'first_name': 'User', 'last_name': 'Three'}
# ]

# # Loop through each user data entry
# for user_data in users_data:
#     # Check if the user already exists
#     user, created = CustomUser.objects.get_or_create(email=user_data['email'],
#                                                      defaults={'password': user_data['password'],
#                                                                'first_name': user_data['first_name'],
#                                                                'last_name': user_data['last_name']})
#     if created:
#         print(f'Created user: {user_data["email"]}')
#     else:
#         print(f'User already exists: {user_data["email"]}')

# # Fetch users from the database after creation
# user1 = CustomUser.objects.get(email='user1@example.com')
# user2 = CustomUser.objects.get(email='user2@example.com')
# user3 = CustomUser.objects.get(email='user3@example.com')

# # Add users to their respective groups
# # Add 'user1' to the 'Editors' group (they can view, create, and edit books and libraries)
# editors_group = Group.objects.get(name='Editors')
# editors_group.user_set.add(user1)

# # Add 'user2' to the 'Viewers' group (they can only view books and libraries)
# viewers_group = Group.objects.get(name='Viewers')
# viewers_group.user_set.add(user2)

# # Add 'user3' to the 'Admins' group (they have full access to books and libraries)
# admins_group = Group.objects.get(name='Admins')
# admins_group.user_set.add(user3)

# # Optional: Verify that the permissions have been correctly assigned to the groups
# editors_permissions = editors_group.permissions.all()
# print(f"Editors group permissions: {[perm.codename for perm in editors_permissions]}")