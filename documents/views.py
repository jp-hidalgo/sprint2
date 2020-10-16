from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .logic.logic_documents import get_all_documents


def get_documents(request):
    documents = get_all_documents()
    documents_list = serializers.serialize('json',documents)
    return HttpResponse(documents_list,content_type='application/json')