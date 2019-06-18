from django.contrib.admin import AdminSite
from django.contrib.admin.options import BaseModelAdmin, ModelAdmin
from django.http import Http404
from django.shortcuts import render
from django.template.response import TemplateResponse

from client.forms import AddBookmarkForm, RemoveBookmarkForm
from middleware.admin import CustomLog
from middleware.models import Log, Client
from django.views.decorators.http import require_POST, require_GET
from jet.models import Bookmark
from jet.utils import JsonResponse

# Create your views here.

def landing_page(request):
    return render(request, 'index.html')

def getUserLogs(request):
    userLogs = Log.objects.filter(client=request.user.id)
    context = {"logs" : userLogs}
    return render(request,'dashboard/index.html', context)



@require_POST
def add_bookmark_view(request):
    result = {'error': False}
    form = AddBookmarkForm(request, request.POST)
    if form.is_valid():
        bookmark = form.save()
        result.update({
            'id': bookmark.pk,
            'title': bookmark.title,
            'url': bookmark.url
        })

    else:
        result['error'] = True

    return JsonResponse(result)


@require_POST
def remove_bookmark_view(request):
    result = {'error': False}

    try:
        instance = Bookmark.objects.get(pk=request.POST.get('id'))
        form = RemoveBookmarkForm(request, request.POST, instance=instance)

        if form.is_valid():
            form.save()
        else:
            result['error'] = True
    except Bookmark.DoesNotExist:
        result['error'] = True

    return JsonResponse(result)


def index(request):
    broker_key = get_broker_key(request.user)
    plan_name = get_plan_name(request.user)
    plan_price = get_plan_price(request.user)
    context = {
        'broker_key' : broker_key,
        'plan_name': plan_name,
        'plan_price' : plan_price,
    }
    return render(request,'dashboard/index.html' , context=context)


def get_broker_key(user):
    return user.client.key

def get_plan_name(user):
    return user.usermembership.membership

def get_plan_price(user):
    return user.usermembership.membership.price
def app_index(request):
    context = {
        'app_list' : True,
    }
    return TemplateResponse(request,  'dashboard/app_index.html' , context=context)


def changelist(request):
    admin_alternative = AdminAlternative(model=Log , admin_site=AdminSite())
    context = admin_alternative.change_list_view(request).context_data
    cl = context["cl"]
    results = Log.objects.filter(client_id=request.user.client.id)
    cl.result_list = results
    cl.result_count = results.count()
    cl.list_display = ('device' , 'status' , 'time')
    return TemplateResponse(request,  'dashboard/change_list.html' , context)


def cancel_subscription(request):
    return TemplateResponse(request , 'dashboard/delete_confirmation.html')

class AdminAlternative(CustomLog):

    def __init__(self , model , admin_site):
        super().__init__(model , admin_site)

    def has_view_or_change_permission(self, request, obj=None):
        return True

    def change_list_view(self , request):
        return  self.changelist_view(request)





