from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        cs=get_token(request)
        if request.user is not None:
            post_list = post.objects.all()
            paginator = Paginator(post_list, 2)  # Show 25 contacts per page

            page = request.GET.get('page')
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            data={"posts": posts, "cs": cs,"username":request.user}

            return render_to_response('index.html', context=data)

        else: render_to_response('login.html',{"cs":cs,"username":request.user})

    def post(self,request):
        cs = get_token(request)
        if request.POST['post_type']=='log':
            email = request.POST['email']
            password = request.POST['password']
            name=User.objects.filter(email=email)[0].username

            user = auth.authenticate(username=name, password=password)
            if user is not None and user.is_active:
                # Правильный пароль и пользователь "активен"
                auth.login(request, user)
                post_list = post.objects.all()
                paginator = Paginator(post_list, 2)  # Show 25 contacts per page

                page = request.GET.get('page')
                try:
                    posts = paginator.page(page)
                except PageNotAnInteger:
                    posts = paginator.page(1)
                except EmptyPage:
                    posts = paginator.page(paginator.num_pages)
                data = {"posts": posts, "cs": cs, "username": request.user}

                return render_to_response('index.html', context=data)
            else:
                return render_to_response('login.html',{"cs":cs})
        elif request.POST['post_type']=='reg':
            email = request.POST['email']
            password = request.POST['password']
            name = request.POST['name']
            user = User.objects.create_user(username=name, email=email, password=password)
            user.profil.country = request.POST['country']
            user.profil.bir_day = request.POST['bir_day']
            user.profil.city = request.POST['city']
            user.save()
            user = auth.authenticate(username=name, password=password)
            if user is not None and user.is_active:
                # Правильный пароль и пользователь "активен"
                auth.login(request, user)
                post_list = post.objects.all()
                paginator = Paginator(post_list, 2)  # Show 25 contacts per page

                page = request.GET.get('page')
                try:
                    posts = paginator.page(page)
                except PageNotAnInteger:
                    posts = paginator.page(1)
                except EmptyPage:
                    posts = paginator.page(paginator.num_pages)
                data = {"posts": posts, "cs": cs, "username": request.user}

                return render_to_response('index.html', context=data)
            else:
                return render_to_response('login.html',{"cs":cs})

        else:
            p = post()
            p.name=request.POST['name']
            try:
                p.image=request.FILES['file']
            except:p.image=request.POST['file']
            p.user_name=request.user

            p.save()

            cs = get_token(request)
            post_list = post.objects.all()
            paginator = Paginator(post_list, 2)  # Show 25 contacts per page

            page = request.GET.get('page')
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            data={"posts": posts, "cs": cs,"username":request.user}
            return render_to_response('index.html', context=data)

def login_form(request):
    cs=get_token(request)
    form=login_form
    return render_to_response('login.html', locals())

def login(user,request):
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        post_list = post.objects.all()
        paginator = Paginator(post_list, 25)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render_to_response('index.html', context={"posts": posts})
    else:
        return render_to_response('login.html')

def registr_form(request):
    form=registration_form()
    cs=get_token(request)
    return render_to_response('registration.html', locals())