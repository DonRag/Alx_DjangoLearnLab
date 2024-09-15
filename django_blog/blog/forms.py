from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
from taggit.forms import TagWidget

# Extend the django in-built UserCreationForm to include email
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Specify model to interact with form and fields to include 
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        # Saves automatically because email is part of in-builder User model fields

# Form allowing users to update their profiles
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_photo', 'interests']

# Form allowing authenticated users to create a post and owners to update a post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include only title, content, and tags fields
        widgets = {
            'tags': TagWidget(),  # Use TagWidget from django-taggit
        }

    #def clean_content(self):
        #content = self.cleaned_data.get('content')
        #if len(content) < 1:
            #raise forms.ValidationError("You cannot add an empty comment!")
        #return content
    
    #def __init__(self, *args, **kwargs):
        # Custom initialization can be added here, if needed
        #super().__init__(*args, **kwargs)

    #def save(self, commit=True, user=None):
        #Override the save method to automatically set the owner of the post
        #post = super().save(commit=False)
        #if user is not None:
            #post.owner = user  # Set the owner to the logged-in user
        #if commit:
            #post.save()
        #return post

# Form allowing authenticated users to write a comment on a post    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Highlighted because the validation is done at the model level to exclude blank comments from being
                    # saved on DB
    # def clean_content(self):
        #content = self.cleaned_data.get('content')
        #if len(content) < 5:
            #raise forms.ValidationError("You cannot add an empty comment!")
        #return content


# For both forms(Post & Comment) django forms validation and saving is not overriden!!