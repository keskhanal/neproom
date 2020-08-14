from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Listing
from staff.models import Staff
from listings.choices import state_choices, price_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(request,'pages/index.html', context)

def about(request):
    staff = Staff.objects.all()

    context = {
        'staff':staff
    }

    return render(request,'pages/about.html', context)