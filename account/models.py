from django.db import models
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            phone=phone,

        )
        user.is_administrator = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(unique=True , max_length=50)
    phone = models.CharField(unique=True , max_length=11)
    is_active = models.BooleanField(default=True)
    is_administrator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username","email"]

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_administrator

class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="Profile")
    first_name = models.CharField(max_length=50, blank=True, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=False)
    nationality_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=False)
    photo = models.ImageField(upload_to='profile_image/')


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=MyUser)



class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('d', 'draft')
    )
    LANGUAGEOFCREATE = (
        ('django','Django'),
        ('djangorest','djangoRestFramework'),
        ('html', 'html&css'),
        ('next', 'nextJs'),
        ('php', 'Php')
    )
    admin = models.ForeignKey(MyUser, related_name="adminUser" , on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.IntegerField(null=False, blank=False)
    time_of_create = models.CharField(max_length=40)
    Language_of_create = models.CharField(max_length=10, choices=LANGUAGEOFCREATE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoryPost")
    image = models.ImageField(upload_to='image_post/')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE , related_name="UserThatBuy")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="PostThatBuy")
    quantity = models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)

