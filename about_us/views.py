from django.shortcuts import render

# Create your views here.

def about_us_view(request):
    return render(request, 'AboutUs.html')
