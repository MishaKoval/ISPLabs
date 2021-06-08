import concurrent.futures
from finalblog import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.core.mail import EmailMessage
from mainblog.models import Post, Role
from .forms import UserRegistrationForm
from .models import Account
import logging
import threading

logger = logging.getLogger(__name__)


def make_new_thread(func, *args, **kwargs):
    new_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    new_thread.start()


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            logger.info("New user registered: " + user_form.cleaned_data["username"])
            email_body = "I'm glad you are here. Welcome to the best blogging website!"
            email_subject = 'Welcome, my friend!'
            email = EmailMessage(email_subject, email_body, 'trueblog89@gmail.com', to=[user_form.cleaned_data["email"]])
            make_new_thread(email.send, fail_silently=False)
            return redirect('login')
        messages.error(request, "invalid data")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': user_form})


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(username + " logged in")
                return redirect('home')
            messages.error(request, "Wrong password")
            logger.info("failed login with username: " + username + "and password: " + password)
            return render(request, 'users/login.html', {})
        except:
            messages.error(request, "No users with this username")
            logger.error("failed login")
            return render(request, 'users/login.html', {})
    else:
        return render(request, 'users/login.html', {})


def my_logout(request):
    if request.method == 'GET':
        logger.info(request.user.username + " logged out")
        logout(request)
        return redirect('home')


class UserDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        us_id = self.request.path.split('/')[2]
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['cur_user'] = User.objects.get(id=us_id)
        context['posts'] = Post.objects.select_related("author").filter(author_id=us_id)
        context['roles'] = Role.objects.prefetch_related("users").filter(users=context['user'])
        context['account'] = Account.objects.select_related("user").filter(user_id=us_id).first()
        return context


def update_account(request, pk):
    if str(request.user.pk) != pk:
        logger.error(request.user.username + " tried to update wrong acc")
        return redirect('home')
    if request.method == 'POST':
        phone = request.POST.get('phone')
        user = User.objects.get(id=pk)
        try:
            if phone is None:
                raise Exception
            if Account.objects.filter(user=user).first() is not None:
                Account.objects.update(user=user, phone=phone)
            else:
                Account.objects.create(user=user, phone=phone)
            logger.info(user.username + "'s new phone is " + phone)
            return redirect('detail_user', pk)
        except:
            messages.error(request, "invalid phone")
            logger.error(user.username + " failed to change phone number")
            return render(request, 'users/edit.html', {})
    else:
        return render(request, 'users/edit.html', {})
