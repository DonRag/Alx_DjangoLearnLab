from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm, PostForm, CommentForm 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post, Comment
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Home page view
class IndexView(TemplateView):
    template_name = 'index.html'

# Register view for users to register and log them in after registeration
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

# User profile view for users to add bio, profile photo, etc.
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user) # Get or create profile for logged in user

    if request.method('POST'):
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {'form': form})

# Login view for users to login
class LoginView(LoginView):
    template_name = 'blog/login.html'
    success_url = reverse_lazy('index')

# Logout view for users to logout
class LogoutView(LogoutView):
    template_name = 'blog/logout.html'
    success_url = reverse_lazy('login')

# View for all posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Path to your template
    context_object_name = 'posts'

# View for listing posts by tag
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'  # Template for displaying posts
    context_object_name = 'posts'
    paginate_by = 10  # Optional: paginate results

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

# View for individual post details 
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Path to your template
    context_object_name = 'post'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')  # Get tag_slug from the URL
        tag = get_object_or_404(Tag, slug=tag_slug)  # Get the tag object, or 404 if it doesn't exist
        return Post.objects.filter(tags__in=[tag])  # Filter posts by the tag

# View for authenticated user to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use the custom form
    #fields = ['title', 'content']
    template_name = 'post_create.html'  # Path to your template
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Set the post owner to the current user
        return super().form_valid(form)

# View for post owner to update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the custom form
    #fields = ['title', 'content']
    template_name = 'post_update.html'  # Path to your template
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # Check if the current user is the owner of the post
        post = self.get_object()
        return post.owner == self.request.user

    def handle_no_permission(self):
        # Custom behavior when test_func returns False
        raise PermissionDenied("You do not have permission to edit this post.")

# View for post owner to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'  # Path to your template
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # Check if the current user is the owner of the post
        post = self.get_object()
        return post.owner == self.request.user

    def handle_no_permission(self):
        # Custom behavior when test_func returns False
        raise PermissionDenied("You do not have permission to delete this post.")
    
# View for all comments
class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'  # Path to your template
    context_object_name = 'comments'

# View for individual comment details 
class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'  # Path to your template
    context_object_name = 'comment'

# View for authenticated user to create a comment on a post
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm  # Use the custom form
    #fields = ['title', 'content']
    template_name = 'comment_create.html'  # Path to your template
    success_url = reverse_lazy('comment_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Set the comment owner to the current user
        return super().form_valid(form)

# View for comment owner to update a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm  # Use the custom form
    #fields = ['title', 'content']
    template_name = 'comment_update.html'  # Path to your template
    success_url = reverse_lazy('comment_list')

    def test_func(self):
        # Check if the current user is the owner of the comment
        comment = self.get_object()
        return comment.owner == self.request.user

    def handle_no_permission(self):
        # Custom behavior when test_func returns False
        raise PermissionDenied("You do not have permission to edit this comment.")

# View for comment owner to delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'  # Path to your template
    success_url = reverse_lazy('comment_list')

    def test_func(self):
        # Check if the current user is the owner of the comment
        post = self.get_object()
        return post.owner == self.request.user

    def handle_no_permission(self):
        # Custom behavior when test_func returns False
        raise PermissionDenied("You do not have permission to delete this comment.")
