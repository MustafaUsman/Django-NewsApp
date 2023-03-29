from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=b896d25d51f153da7166d3b4011f7fbb&countries=au')
    res = r.json()
    data = res['data']
    title = []
    description = []
    url = []
    image = []
    for i in range(len(data)):
        title.append(data[i]['title'])
        description.append(data[i]['description'])
        url.append(data[i]['url'])
        image.append(data[i]['image'])
    news = zip(title, description, url, image)
    return render(request, 'newsapp/index.html', {'news': news})    

def login(request):
    return render(request, 'newsapp/login.html')

    