from typing import Dict, Any

from django.db.models import Manager, QuerySet

from ..querysets import CustomerQuerySet


class CustomerManager(Manager):
    def get_queryset(self, **kwargs) -> CustomerQuerySet:
        return CustomerQuerySet(self.model, using=self._db)

    def annotate_with_spent_money(self) -> QuerySet:
        return self.get_queryset().annotate_with_spent_money()

    def get_top_customers(self):
        return self.get_queryset().get_top_customers()

    def annotate_with_top_gems(self):
        return self.get_queryset().annotate_with_top_gems()
