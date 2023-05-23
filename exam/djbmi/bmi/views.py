from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import People

# Create your views here.

def main(request):
    template = loader.get_template('main.html')
    context = {
        'title': 'BMI Calculator',
    }
    return HttpResponse(template.render(context, request))

def allpeople(request):
    AllPeople = People.objects.all().values()
    template = loader.get_template('index.html')
    for people in AllPeople:
        people['bmi'] = round(people['weight'] / (people['tall'] / 100) ** 2, 2)
    context = {
        'people': AllPeople,
    }
    return HttpResponse(template.render(context, request))

def details(request, ssn):
    this_people = People.objects.get(ssn = ssn)
    template = loader.get_template('details.html')
    this_people.bmi = round(this_people.weight / (this_people.tall / 100) ** 2, 2)
    context = {
        'people': this_people,
    }
    return HttpResponse(template.render(context, request))