from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

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
    'december': 'Walk for 130 minutes'
}

def month_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound()
    months = list(challenges.keys())
    month_string = months[month-1]
    return HttpResponseRedirect(f'/challenges/{month_string}')

def month(request, month):
    challenge_text = challenges.get(month.lower())
    if challenge_text is None:
        return HttpResponseNotFound('Month not found')
    return HttpResponse(challenge_text)
