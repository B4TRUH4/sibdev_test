from typing import Any

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import QuerySet, Sum, DecimalField
from django.db.models.functions import Coalesce

from ...constants import CustomerConstants


class CustomerQuerySet(QuerySet):
    def annotate_with_spent_money(self) -> QuerySet:
        """
        Добавляет поле общей потраченной суммы
        :return: QuerySet с полем общей потраченной суммы
        """
        return self.annotate(
            spent_money=Coalesce(
                Sum('deals__total'),
                0,
                output_field=DecimalField(),
            ),
        )

    def get_top_customers(self, amount=CustomerConstants.TOP_CUSTOMERS_AMOUNT):
        """
        Возвращает указанное количество покупателей
        с наибольшими затратами за весь период
        :param amount: количество покупателей
        :return: QuerySet из amount покупателей
        """
        return self.order_by('-spent_money')[:amount]

    def annotate_with_top_gems(
            self, amount=CustomerConstants.MIN_GEM_AMOUNT) -> list[Any]:
        """
        Добавляет поле со списком названий камней,
        которые купили как минимум amount из входного списка
        :param amount: количество человек, которые должны
                       купить камень
        :return: список покупателей с камнями
        """
        queryset = self.annotate(
            gems=ArrayAgg('deals__item__name', distinct=True),
        )

        gem_counter = {}
        data = list(queryset.values())
        for customer in data:
            for gem in customer["gems"]:
                if gem in gem_counter:
                    gem_counter[gem] += 1
                else:
                    gem_counter[gem] = 1

        for customer in data:
            new_gems = []
            for gem in customer['gems']:
                if gem_counter[gem] >= amount:
                    new_gems.append(gem)
            customer['gems'] = new_gems

        return data
