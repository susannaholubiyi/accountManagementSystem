from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account
from .serializers import AccountSerializer

from django.shortcuts import render


# Create your views here.
@api_view()
def list_account(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response("hi")


def account_detail(request, pk):
    return HttpResponse(pk)
