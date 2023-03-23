from django.urls import path
from .views import *

urlpatterns = [
    # для повара

    path('orders/cook/', OrdersCookViewList.as_view()),
    path('orders/cook/<int:pk>/', OrdersCookUpdate.as_view()),

    # для официанта

    path('orders/waiter/<int:pk>/', OrdersWaiterCRUD.as_view()),
    path('orders/waiter/', OrdersWaiterViewList.as_view()),

    # для админа

    path('orders/admin/', OrdersAdminView.as_view()),
    path('shifts/', ShiftList.as_view()),
    path('shift/<int:pk>/', ShiftUpdate.as_view()),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>/', GroupUpdate.as_view()),
    path('groups/', GroupList.as_view()),
    path('employees/', EmployeeList.as_view()),
    path('employee/<int:pk>', EmployeeUpdate.as_view()),

]
