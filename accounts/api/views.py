# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
#
#

#
#
# class AccountListView(ListAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountSerializer
#
#
# class AccountDetailView(RetrieveAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountSerializer
#
#
# class AccountCreateView(CreateAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountSerializer
#
#
# class AccountUpdateView(UpdateAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountSerializer
#
#
# class AccountDeleteView(DestroyAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountSerializer
from rest_framework import viewsets

from accounts.models import Accounts
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Accounts.objects.all()