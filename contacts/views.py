from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        tenant_email = request.POST['tenant_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'already made an inquery for this room. ')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id,
                    name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        send_mail(
            'Room listing Inquery',
            'There has been inquery for ' + listing + '. sign in to the admin panel for more info.',
            'yourtutor2077@gmail.com',
            [tenant_email, 'keskhanal2413@gmail.com'],
            fail_silently=False  

        )

        messages.success(request, "Your request has been submitted, a tenant will get back to you soon. ")
        return redirect('/listing/'+ listing_id)