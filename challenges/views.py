from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Challenge, Month, ChallengeMonth


def index(request):
    months = Month.objects.all().order_by('code')
    return render(request, 'challenges/index.html', {
        'months': months
    })


def month_by_number(request, month):
    try:
        month_obj = Month.objects.get(code=month)
        print(month_obj)
        redirect_path = reverse('month', args=[month_obj.name])
        return HttpResponseRedirect(redirect_path)
    except Month.DoesNotExist:
        return HttpResponseNotFound()


def month(request, month):
    month_obj = get_object_or_404(Month, name=month)

    try:
        challenge_month = ChallengeMonth.objects.get(month=month_obj)
        challenge_text = challenge_month.challenge.name
    except ChallengeMonth.DoesNotExist:
        # Month exists but has no challenge (like December)
        challenge_text = None

    return render(request, 'challenges/challenge.html', {
        'month': month,
        'text': challenge_text
    })