from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from main.models import ManiCatigorey
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Categorey(models.Model):
    main=models.ForeignKey(ManiCatigorey, on_delete=models.CASCADE)
    name=models.CharField(max_length=250, help_text="categoriya kiriting masalan suzus, sport va hakoza", unique=True)
    slug=models.SlugField(max_length=250, help_text='sulug takrorlanmas!!!')
    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name

class PostQuerySet(models.QuerySet):
    def SUNGI(self):
        return self.filter(status=Post.Status.SUNGI)
    def OXIRGI(self):#oxirgi
        return self.filter(status=Post.Status.OXIRGI)
    def FAN_TEXNIKA(self):
        return self.filter(status=Post.Status.FAN_TEXNIKA)
    
    def Mashhur_Yangiliklar(self):
        return self.filter(status=Post.Status.Mashhur_Yangiliklar)
    def ENG_SARA(self):
        return self.filter(status=Post.Status.ENG_SARA)

class PostManager(models.Model):
    def get_queryset(self):
        return PostQuerySet(self.model).filter(active=True)
    def SUNGI(self): #so'ngi yangilik
        return self.get_queryset.SUNGI()
    
    def FAN_TEXNIKA(self):#fan texnalogiya
        return self.get_queryset.FAN_TEXNIKA()
    
    def Mashhur_Yangiliklar(self):#mashhur yangiliklar
        return self.get_queryset.Mashhur_Yangiliklar()
    def ENG_SARA(self): #engsara
        return self.get_queryset.ENG_SARA()
    def OXIRGI(self): #oxirgi
        return self.get_queryset.OXIRGI()
class Post(models.Model):
    class Status(models.TextChoices):
        ENG_SARA='ENS','ENG_SARA'
        Mashhur_Yangiliklar='MAY','MashhurYangiliklar'
        SUNGI='SUN','Sungi'
        FAN_TEXNIKA='FTX',"Fan va Texnalogiya"
        OXIRGI='OX','Oxirgi Maqolalar'
    title=models.CharField(max_length=250, help_text="Sarlavha")
    slug=models.SlugField(max_length=250, help_text='sulug takrorlanmas!!!')
    body=RichTextUploadingField(help_text="Sarlavha davome")
    image=models.ImageField(upload_to='post/%y/%m/%d')
    main=models.ForeignKey(ManiCatigorey, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status=models.CharField(max_length=3, choices=Status.choices, default=Status.OXIRGI)
    categorey=models.ForeignKey(Categorey, on_delete=models.CASCADE, null=True)
    
    tag=models.ManyToManyField('Tag')
    active=models.BooleanField(default=True)
    publish=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
   
    objects = PostQuerySet.as_manager()
    available_active=PostManager()
    def save(self, *args, **kwargs):
        if not self.slug:
           self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-publish']
        indexes = [
        models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('myapp:Post_details', args=[self.slug,
                                                   self.publish.year,
                                                   self.publish.month,
                                                   self.publish.day,
                                                   ])
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body= RichTextField(help_text="Yangi Hablar Yozish!")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
