from _decimal import Decimal

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account, Transaction
from .serializers import AccountSerializer, CreateAccountSerializer
from rest_framework import status

from django.shortcuts import render, get_object_or_404


# Create your views here.
@api_view(['GET', 'POST'])
def list_account(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CreateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CreateAccountSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = CreateAccountSerializer(account, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def deposit(request):
    account_number = request.data['account_number']
    amount = request.data.get('amount', 'amount cannot be null')
    account = get_object_or_404(Account, pk=account_number)
    account.balance += Decimal(amount)
    account.save()
    Transaction.objects.create(
        account=account,
        amount=amount,
        transaction_type='DEB'
    )
    return Response(data={"message": "Transaction successful"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def withdraw(request):
    account_number = request.data['account_number']
    amount = request.data.get('amount', 'amount cannot be null')
    account = get_object_or_404(Account, pk=account_number)
    pin = request.data['pin']
    if account.pin == pin:
        if account.balance > amount:
            account.balance -= Decimal(amount)
            account.save()
            Transaction.objects.create(
                account=account,
                amount=amount
            )
        else:
            return Response(data={"message": "Insufficient amount"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(data={"message": "Invalid pin"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={"message": "Transaction successful"}, status=status.HTTP_200_OK)

