from django.shortcuts import render
from django.utils import timezone, datetime_safe
from os import environ

experience = [
    {"date": "Decemeber 2, 2019 - January 31, 2020",
     "exp": "Google Code-In",
     'new_period': '2019-2020',
     "as": "Finalist",
     "desc": "Got selected as a Finalist for the organization BRL-CAD."},
    {"date": "Decemeber 2, 2019 - Present",
     "exp": "BRL-CAD",
     "as": "Contributor",
     "desc": "Contributing to BRL-CAD project on Sourceforge."},
    {"date": "October 4, 2020 - Present",
     'new_period': '2020-2021',
     "exp": "Zulip Terminal",
     "as": "Contributor",
     "desc": "Contributing to Zulip Terminal project on Github."},
]
direc = list()
for i in range(0, len(experience)):
    direc.append("left" if i % 2 == 0 else "right")
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
    return render(request, 'site/about.html', {'age': age, "if_distill": if_distill, "list": zip(experience, direc)})
