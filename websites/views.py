from django.shortcuts import render


def home_page(request):
    return render(request, 'websites/home_page.html')


def reg_page(request):
    return render(request, 'websites/reg_page.html')
