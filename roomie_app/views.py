from django.shortcuts import render,get_object_or_404, redirect
from .models import Category, Ad, Roommates
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import PostForm
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.views.generic.edit import DeleteView

def home_page(request):
    categories = Category.objects.all()
    adds = Ad.objects.all()

    context = {
    'categories': categories,
    'adds': adds
    }

    return render(request, "./home.html", context)


def ads_page(request):
    adds = Ad.objects.all()
    context = {
        'adds': adds
    }
    return render(request, 'ads.html', context)

def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)    

def favorite_page(request):
    adds = Ad.objects.all()
    context = {
        'adds': adds
    }
    return render(request, 'favorite.html', context)  


def neighbor_page(request):
    roommates = Roommates.objects.all()
    context = {
        'roommates': roommates
    }
    return render(request, 'neighbor.html', context)  

def neighbor_detail_page(request, pk):  
    roommates = get_object_or_404(Roommates, pk=pk) 
    context = {
        'roommates': roommates
    }
    return render(request, "neighbor_detail.html", context)


def ads_detail_page(request, pk):  
    adds = get_object_or_404(Ad, pk=pk) 
    context = {
        'adds': adds
    }
    return render(request, "ads_detail.html", context)


def ads_by_categories_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    adds=Ad.objects.filter(category=category)
    context = {
        'categories': category,
        'adds': adds
    }
    return render(request, "./ads-by-category.html", context)




def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form= NewUserForm()
        context={
            'form':form
        }
        return render(request, "sign-up.html", context)

def login_page(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')  
            user = authenticate( username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

        context={
            'form':form
        }    
        return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')



def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Пост успешно добавлен!")
            return redirect('home_page') 
        else:
            messages.error(request, "Ошибка при добавлении поста. Пожалуйста, попробуйте снова.")
    else:
        form = PostForm()

    return render(request, 'create_ad.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(Ad, id=post_id)
    if post.author != request.user:  # Проверяем, является ли пользователь автором
        return HttpResponseForbidden("Вы не можете удалить этот пост.")
    
    post.delete()
    return redirect('home_page')