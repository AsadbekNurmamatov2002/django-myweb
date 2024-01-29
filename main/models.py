from django.utils.text import slugify
from django.db import models
# Create your models here.
class ManiCatigorey(models.Model):
    name=models.CharField(max_length=250, help_text="Main Katigoryani kiriting masalan Chetil va boshga, yani Navbar da turovchi ckatigorya", unique=True)
    def __str__(self) -> str:
        return self.name

class Boglanish(models.Model):
    manzil=models.URLField(max_length=200,help_text="URL manzili!!")
    soni=models.IntegerField(help_text='Obunachilar soni ixtiyoriy!!!',null=True, blank=True)
    icons=models.CharField(max_length=400, help_text='icon kiriting!! : Masalan: facebook-( fa fa-facebook ),twitter-( fa fa-twitter ), linkedin-( fa fa-linkedin ), rss-( fa fa-rss )')
    def __str__(self) -> str:
        return self.icons
    

class Reclama(models.Model):
    title=models.CharField(max_length=250, null=True, blank=True)
    body=models.TextField(null=True, blank=True)
    manzil=models.URLField(max_length=400, null=True, blank=True)
    image=models.ImageField(upload_to='Reclama/%y/%m/%d/', null=True, blank=True)
    def __str__(self) -> str:
        return self.title

class Navbar(models.Model):
    logo=models.CharField(max_length=25)
    footer=models.CharField(max_length=50)
    color=models.CharField(max_length=250, null=True, blank=True, help_text="font rangi misol: red, #3333, #ffff, #dgdyu5")
    fonts=models.CharField(max_length=250, null=True, blank=True, help_text="fontni: https://fonts.googleapis.com/css?family=Sofia dan oloning!!!")
    size=models.CharField(max_length=250, null=True, blank=True, help_text="font o'lchavi yani px sillarda beriladi!!! masalan: 16px ,32px , 72px ,91px")
    class Meta:
        ordering=['-id']
    def __str__(self) -> str:
        return self.logo
