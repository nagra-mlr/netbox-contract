from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # Contracts
    path('contracts/', views.ContractListView.as_view(), name='contract_list'),
    path('contracts/add/', views.ContractEditView.as_view(), name='contract_add'),
    path('contracts/<int:pk>/', views.ContractView.as_view(), name='contract'),
    path('contracts/<int:pk>/edit/', views.ContractEditView.as_view(), name='contract_edit'),
    path('contracts/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),
    path('contracts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='contract_changelog', kwargs={
        'model': models.Contract
    }),

    # Contract invoices
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/add/', views.InvoiceEditView.as_view(), name='invoice_add'),
    path('invoices/<int:pk>/', views.InvoiceView.as_view(), name='invoice'),
    path('invoices/<int:pk>/edit/', views.InvoiceEditView.as_view(), name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
    path('invoices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='invoice_changelog', kwargs={
        'model': models.Invoice
    }),


)