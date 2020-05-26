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
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원
    """
    serializer_class = AccountSerializer
    queryset = Accounts.objects.all()