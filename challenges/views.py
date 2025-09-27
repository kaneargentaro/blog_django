from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items=""
    months = list(challenges.keys())

    for month in months:
        capitalised_month = month.capitalize()
        month_path = reverse('month', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalised_month}</li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)

def month_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound()
    months = list(challenges.keys())
    redirect_month = months[month-1]
    redirect_path = reverse('month', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def month(request, month):
    challenge_text = challenges.get(month.lower())
    if challenge_text is None:
        return HttpResponseNotFound('Month not found')
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
