
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from .models import Contract,Invoice,ServiceProvider

class ContractFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Contract
        fields = ('id', 'external_partie', 'internal_partie', 'status','circuit')

    def search(self, queryset, name, value):
        return queryset.filter( Q(name__icontains=value) 
                               | Q(circuit__cid__icontains=value) 
                               | Q(external_partie__name__icontains=value))

class InvoiceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Invoice
        fields = ('id', 'contracts')

    def search(self, queryset, name, value):
        return queryset.filter(Q(number__icontains=value)
                               | Q(contracts__name__icontains=value))

class ServiceProviderFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = ServiceProvider
        fields = ('id','name')

    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
