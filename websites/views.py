from django.shortcuts import render


def home_page(request):
    return render(request, 'websites/home_page.html')
