from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    import random

    pwd = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    num = '1234567890'
    spec_chars = '!@#$%'

    chars = list(alpha)
    length = int(request.GET.get('length', 12))

    while int(request.GET.get('length')) > 25:
        return render(request, 'generator/home.html')

    if request.GET.get('upper') == 'on':
        chars.extend(alpha.upper())

    if request.GET.get('nums') == 'on':
        chars.extend(num)

    if request.GET.get('schars') == 'on':
        chars.extend(spec_chars)

    for x in range(length):
        pwd += random.choice(chars)

    return render(request, 'generator/password.html', {"password": pwd})


def about(request):
    import datetime

    date = datetime.datetime.now()

    return render(request, 'generator/about.html', {"date": date})
