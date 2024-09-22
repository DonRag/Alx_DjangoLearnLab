# accounts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Importing the CustomUser model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    # Add a method to handle GET requests
    def get(self, request, *args, **kwargs):
        return Response({"message": "Register form (or page) is here"}, status=200)

class LoginView(ObtainAuthToken):
    # Custom login view to return token and user info
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = UserSerializer(token.user)
        return Response({
            'token': token.key,
            'user': user.data
        })

    # Add a method to handle GET requests
    def get(self, request, *args, **kwargs):
        return Response({"message": "Login form (or page) is here"}, status=200)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the current user
        return self.request.user
    
    # Add a method to handle GET requests
    def get(self, request, *args, **kwargs):
        return Response({"message": "Profile page is here"}, status=200)

# Follow User View using GenericAPIView
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can follow others

    def post(self, request, user_id):
        # Get the user the current user wants to follow using CustomUser.objects.all()
        user_to_follow = get_object_or_404(User.objects.all(), id=user_id)

        # Prevent following yourself
        if request.user == user_to_follow:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the current user's 'following' list
        request.user.following.add(user_to_follow)

        # Return a success message
        return Response({'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


# Unfollow User View using GenericAPIView
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can unfollow others

    def post(self, request, user_id):
        try:
            # Get the user the current user wants to unfollow using CustomUser.objects.all()
            user_to_unfollow = get_object_or_404(User.objects.all(), id=user_id)

            # Remove the user from the current user's 'following' list
            request.user.following.remove(user_to_unfollow)
        except User.DoesNotExist:
            # Return a success message
            return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
