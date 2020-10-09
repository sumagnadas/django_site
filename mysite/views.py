from django.shortcuts import render
from django.utils import timezone, datetime_safe
from os import environ

experience = [
    {"date": "Decemeber 2, 2019",
     "exp": "Google Code-In",
     "as": "Finalist",
     "desc": "Got selected as a Finalist for the organization <italic>BRL-CAD</italic>."}
]
if_distill = "DISTILL_GEN" in environ

def index(request):
    timezone.activate(timezone.get_current_timezone())
    birth_date = datetime_safe.datetime(2006, 1, 11, tzinfo=timezone.get_current_timezone())
    age = (timezone.now() - birth_date).days // 365
    return render(request, 'site/index.html', {'age': age, "if_distill": if_distill})


def about(request):
    timezone.activate(timezone.get_current_timezone())
    birth_date = datetime_safe.datetime(2006, 1, 11, tzinfo=timezone.get_current_timezone())
    age = (timezone.now() - birth_date).days / 365
    if age > ((timezone.now() - birth_date).days // 365):
        age = str(int(age)) + "+"
    return render(request, 'site/about.html', {'age': age, "experience": experience, "if_distill": if_distill})
