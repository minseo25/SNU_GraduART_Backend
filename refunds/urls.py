from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.request_refund, name='request_refund'),
    path('<uuid:item_id>/', views.refund_status, name='refund_status'),
]

