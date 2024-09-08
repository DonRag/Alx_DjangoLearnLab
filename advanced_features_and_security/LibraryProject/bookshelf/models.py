from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

        

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.role}'


class Author(models.Model):
    name = models.CharField(max_length=100)
        

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    author = models.ForeignKey( Author, on_delete=models.CASCADE, related_name='books')
    
    class Meta:
        permissions = [
            ("can_view_book","Can view book"),   
            ("can_create_book","Can create book"),   
            ("can_edit_book","Can edit book"),   
            ("can_delete_book","Can delete book"),   
        ]
        
    def __str__(self) -> str:
        return f"{self.title} by {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(
        Book, related_name='libraries'
    )
    
    class Meta:
        permissions = [
            ("can_view_library", "Can view library"),
            ("can_create_library", "Can create library"),
            ("can_edit_library", "Can edit library"),
            ("can_delete_library", "Can delete library"),
        ]
    
    def __str__(self) -> str:
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.library.name} - Librarian"
