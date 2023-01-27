from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email')
        email = self.model(email=email)
        email.set_password(password)
        email.save(using=self._db)
        return email

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('Email', max_length = 100, unique=True)
    password = models.CharField('Password', max_length = 200, validators=[RegexValidator(regex='^(?=.?[A-Z])(?=.?[a-z])(?=.*?[!@#?\]^]).{10,}$', 
                                                                                                message=' A valid password MUST contains at least 10 characters, one lowercase letter, one uppercase letter and one of the following characters: !, @, #, ? or ]', 
                                                                                                code='nomatch')])
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    def natural_key(self):
        return (self.email)

    objects = UserManager()
    USERNAME_FIELD = 'email'
