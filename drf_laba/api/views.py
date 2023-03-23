from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import *
from .permissions import IsCook, IsAdmin, IsWaiter

# для повара
class OrdersCookUpdate(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCook, )


class OrdersCookViewList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCook, )

# для админа

class OrdersAdminView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdmin, )

# для официанта

class OrdersWaiterViewList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsWaiter, )


class OrdersWaiterCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsWaiter, )

# для админа

class ShiftList(ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdmin, )


class ShiftUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdmin, )


class GroupList(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdmin, )


class GroupUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdmin, )


class EmployeeList(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdmin, )


class EmployeeUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdmin, )