from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categorey, Message
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('myapp:home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Bunday Foydalanovchi Topilmadi!')

        user = authenticate(request, email=email, password=password) 

        if user is not None:
            login(request, user)
            return redirect('myapp:home')
        else:
            messages.error(request, 'Parol yoke Email xato!')

    context = {'page': page}
    return render(request, 'authlogin/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('myapp:home')


def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('myapp:home')
        else:
            messages.error(request, 'Ro\'yxattdan o\'tishda nimagir xato ketti!')

    return render(request, 'authlogin/login_register.html', {'form': form})

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'authlogin/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'authlogin/update-user.html', {'form': form})

def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print(q)
    posts=Post.objects.filter(Q(title__icontains=q) |
                              Q(categorey__name__icontains=q) |
                              Q(body__icontains=q)).order_by('-created')
    categorey=Categorey.objects.all()
    messages=Message.objects.all()
    context={'posts':posts, 'categorey':categorey, 'messages':messages}
    return render(request, 'index.html', context)

def Post_details(request, slug, year, month, day):
    categorey=Categorey.objects.all()
    post=get_object_or_404(Post, slug=slug, publish__year=year,publish__month=month, publish__day=day)
    messages=Message.objects.all().order_by('-created')
    
    if request.method == 'POST' and not None:
        if request.user.is_authenticated:
            message = Message.objects.create(
                user=request.user,
                post=post,
                body=request.POST.get('body')
            )
            return redirect('myapp:Post_details', slug=post.slug,year=post.publish.year,month=post.publish.month, day=post.publish.day)
        else:
            return redirect('myapp:login')
    return render(request, "details/post_details.html", {'post':post,'forms':forms,'messages':messages, 'categorey':categorey})


def post_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    post_list=Post.objects.filter(Q(title__icontains=q) |
                                  Q(categorey__slug__icontains=q) |
                                  Q(categorey__name__contains=q) |
                                  Q(body__icontains=q)).order_by('-created')
    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'post_list.html',{'posts': posts})


# custom 404 view
def handler404(request, exception):
    return render(request, '404.html', status=404)