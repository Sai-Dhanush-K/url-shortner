from django.contrib.auth.base_user import BaseUserManager

class CoustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier for 
    authentication instead of usernames.
    """
    def create_user(self,email,password, **kwargs):
        if (not email):
            raise ValueError("User must have an Email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)

        if not kwargs.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not kwargs.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **kwargs)

        