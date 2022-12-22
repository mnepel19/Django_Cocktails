from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Cocktail


def index(request):
    cocktail_list = Cocktail.objects.order_by('voltage')[:5]
    template = loader.get_template('cocktails/index.html')
    context = {
        'cocktail_list': cocktail_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, cocktail_id):
    try:
        cocktail = Cocktail.objects.get(pk=cocktail_id)
    except Cocktail.DoesNotExist:
        raise Http404('Cocktail does not exist')
    context = {
                'cocktail_name': cocktail.name,
                'cocktail_voltage': cocktail.voltage
    }
    return render(request, 'cocktails/details.html', context)
