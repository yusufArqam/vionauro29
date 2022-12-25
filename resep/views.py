from blog.models import Artikel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password

from blog.models import Artikel
from user.models import Biodata
import requests

def home(request):
    template_name = 'front/home.html'
    context = {
        'title':'my home',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)

def blog_post(request):
    template_name = 'front/blog-post.html'
    context = {
        'title':'about me',
        'welcome':'ini page about',
    }
    return render(request, template_name, context)
# def blog_page(request):
#     template_name = 'front/blog-page.html'
#     artikel = Artikel.objects.all()
#     context = {
#         'title':'Blog me',
#         'welcome':'ini page about',
#         'artikel' : artikel
#     }
#     return render(request, template_name, context)
def blog_page(request):
    url = "https://masak-apa-tomorisakura.vercel.app/api/recipes"

    data = requests.get(url).json()

    a = data['results']
    title = []
    porsi = []
    kunci = []
    waktu = []
    tingkat =[]
    gambar = []

    for i in range(len(a)):
        f = a[i]
        porsi.append(f['serving'])
        title.append(f['title'])
        kunci.append(f['key'])
        tingkat.append(f['difficulty'])
        waktu.append(f['times'])
        gambar.append(f['thumb'])

    mylist = zip(title, porsi, kunci,waktu, tingkat,gambar)
    context ={'mylist':mylist}

    return render(request, 'front/blog-page.html', context)

def base(request):
    template_name = 'front/base.html'
    context = {
        'title':'Tabel',
    }
    return render(request, template_name, context)

def about_us(request):
    template_name = 'front/about-us.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def contact_us(request):
    template_name = 'front/contact-us.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def isi(request):
    template_name = 'front/isi.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('home')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)


