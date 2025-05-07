from django.shortcuts import render

# Create your views here.
def local_weather(request):
    return render(request, 'local_weather/index.html')