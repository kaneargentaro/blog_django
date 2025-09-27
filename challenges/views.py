from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

challenges = {
    'january': 'Walk for 20 minutes',
    'february': 'Walk for 30 minutes',
    'march': 'Walk for 40 minutes',
    'april': 'Walk for 50 minutes',
    'may': 'Walk for 60 minutes',
    'june': 'Walk for 70 minutes',
    'july': 'Walk for 80 minutes',
    'august': 'Walk for 90 minutes',
    'september': 'Walk for 100 minutes',
    'october': 'Walk for 110 minutes',
    'november': 'Walk for 120 minutes',
    'december': None
}


def index(request):
    months = list(challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


def month_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound()
    months = list(challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse('month', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month(request, month):
    challenge_text = challenges.get(month.lower())
    return render(request, 'challenges/challenge.html', {
        'month': month,
        'text': challenge_text
    })
