from django.db import models

from django_tenants.models import TenantMixin, DomainMixin

class Church(TenantMixin):
    name = models.CharField(max_length=100)

class Domain(DomainMixin):
    pass
