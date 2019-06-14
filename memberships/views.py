from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Membership, UserMembership, Subscription
from django.conf import settings
import stripe
import time
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None


def post(request):
    selected_membership_type = request.POST.get('membership_type')
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    selected_membership_qs = Membership.objects.filter(
        membership_type=selected_membership_type
    )
    if selected_membership_qs.exists():
        selected_membership = selected_membership_qs.first()
    if user_membership.membership.membership_type == selected_membership:
        if user_subscription is not None:
            messages.info(request, """You already have this membership. Your
                                  next payment is due {}""".format('get this value from stripe'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # assign to the session
    request.session['selected_membership_type'] = selected_membership.membership_type

@login_required
def selectMemberShip(request):
    if request.method == 'POST':
        post(request)
        return HttpResponseRedirect(reverse('payment'))

    print(get_user_subscription(request))
    usage = stripe.UsageRecord.create(
        quantity=1,
        timestamp=int(time.time()) ,
        subscription_item=get_user_subscription(request).stripe_subscription_item_id,
        action='increment'
    )
    print(stripe.Invoice.upcoming(customer=request.user.usermembership.stripe_customer_id))
    print(stripe.Customer.list(limit=3))
    item = stripe.SubscriptionItem.retrieve("si_FFbu6n9jJNtknL")
    item.usage_record_summaries(limit=3)
    #todo usage meter
    #todo subscribe free member when login to get subscribe item id
    #todo use usage record in api call
    membership = Membership.objects.all()
    current_membership = get_user_membership(request)
    context = {
        'memberships': membership,
        'current_membership': current_membership.membership.membership_type
    }
    return render(request, 'memberships/memberships.html', context=context)

@login_required()
def payment(request):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            customer.source = token # 4242424242424242
            customer.save()
            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    { "plan": selected_membership.stripe_plan_id },
                ]
            )
            return redirect(reverse('update-transactions',
                                    kwargs={
                                        'subscription_id': subscription.id,
                                        'stripe_subscription_item_id': subscription['items']['data'][0]['id']
                                    }))
        except:
            messages.info(request, "An error has occurred, investigate it in the console")

    context = {
        'publish_key': publish_key,
        'selected_membership': selected_membership
    }
    return render(request, 'memberships/payment.html', context=context)

@login_required()
def updateTransactionRecords(request, subscription_id,stripe_subscription_item_id):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()

    sub, created = Subscription.objects.get_or_create(
        user_membership=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.stripe_subscription_item_id = stripe_subscription_item_id
    sub.active = True
    sub.save()

    try:
        del request.session['selected_membership_type']
    except:
        pass
    messages.info(request, 'Successfully created {} membership'.format(
        selected_membership))
    return redirect('/memberships')
