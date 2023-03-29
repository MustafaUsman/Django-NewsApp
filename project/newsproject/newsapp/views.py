from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login

# Create your views here.
def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=b896d25d51f153da7166d3b4011f7fbb&countries=es')
    res = r.json()
    data = res['data']
    title = []
    description = []
    url = []
    image = []
    published_at=[]
    for i in range(len(data)):
        title.append(data[i]['title'])
        description.append(data[i]['description'])
        url.append(data[i]['url'])
        image.append(data[i]['image'])
        published_at.append(data[i]['published_at'])
    news = zip(title, description, url, image, published_at)
    return render(request, 'newsapp/index.html', {'news': news})    

def Homepage(request):
    pass

def signuppage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        pass2 = request.POST['password2']
        print(username, email, password, pass2)
        if password == pass2:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # print('user created')
            user.save()
            return redirect('login')
            #show a alert that user has been created
            
        else:
            print('password not matching')
            return HttpResponse('password not matching')
        
    return render(request, 'newsapp/signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('user not found')
    return render(request, 'newsapp/login.html')

