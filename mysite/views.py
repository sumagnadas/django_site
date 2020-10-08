from django.shortcuts import render
from django.utils import timezone, datetime_safe


def index(request):
    timezone.activate(timezone.get_current_timezone())
    birth_date = datetime_safe.datetime(2006, 1, 11, tzinfo=timezone.get_current_timezone())
    age = (timezone.now() - birth_date).days // 365
    return render(request, 'site/index.html', {'age': age})


def about(request):
    return render(request, 'site/about.html')
