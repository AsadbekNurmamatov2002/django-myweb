# Generated by Django 5.0.1 on 2024-01-27 04:42

import ckeditor.fields
import ckeditor_uploader.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='categoriya kiriting masalan suzus, sport va hakoza', max_length=250, unique=True)),
                ('slug', models.SlugField(help_text='sulug takrorlanmas!!!', max_length=250)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.manicatigorey')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Sarlavha', max_length=250)),
                ('slug', models.SlugField(help_text='sulug takrorlanmas!!!', max_length=250)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(help_text='Sarlavha davome')),
                ('image', models.ImageField(upload_to='post/%y/%m/%d')),
                ('status', models.CharField(choices=[('ENS', 'ENG_SARA'), ('MAY', 'MashhurYangiliklar'), ('SUN', 'Sungi'), ('FTX', 'Fan va Texnalogiya'), ('OX', 'Oxirgi Maqolalar')], default='OX', max_length=3)),
                ('active', models.BooleanField(default=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('categorey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.categorey')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.manicatigorey')),
                ('tag', models.ManyToManyField(to='myapp.tag')),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(help_text='Yangi Hablar Yozish!')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.post')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='myapp_post_publish_ef79b7_idx'),
        ),
    ]