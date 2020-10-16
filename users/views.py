from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .logic.logic_users import get_all_users


def get_users(request):
    users = get_all_users()
    user_list = serializers.serialize('json',users)
    return HttpResponse(user_list,content_type='application/json')