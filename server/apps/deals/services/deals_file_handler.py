import csv
from typing import Optional, Any, Iterable, Union

from rest_framework import serializers

from ..models import Customer, Gem
from ..serializers import DealCreateSerializer
from ..constants import HandlerErrorsConstants


class DealFileHandler:
    """
    Обработчик csv-файлов сделок
    """
    def __init__(self, file=None):
        self.deals = []
        self.file = file

    def import_data_from_csv_file(self) -> Union[Optional[list], Optional[str]]:
        """
        Метод обработки и сохранения данных из файла
        :return: ошибки
        """
        if not self.file:
            return HandlerErrorsConstants.FILE_NOT_SPECIFIED
        errors, self.deals = self.read_data()
        if errors:
            return errors
        self.save_data()

    def read_data(self) -> (dict[str, Any], dict[str, Any]):
        """
        Метод чтения данных из файла
        :return: ошибки и прочитанные данные
        """
        try:
            reader: Iterable = csv.DictReader(
                self.file.read().decode('utf-8').splitlines()
            )
        except Exception as e:
            return (
                f'{HandlerErrorsConstants.READER_CREATING_ERROR}: {e}',
                self.deals
            )

        errors = []

        for deal in reader:
            item_temp, customer_temp = deal.pop('item'), deal.pop('customer')
            serializer = DealCreateSerializer(data=deal)
            try:
                serializer.is_valid(raise_exception=True)
                deal['item'] = item_temp
                deal['customer'] = customer_temp
                self.deals.append(deal)
            except serializers.ValidationError as e:
                errors.append({
                    'row': deal,
                    'details': e.detail
                })
                continue
        return errors, self.deals

    def save_data(self):
        """
        Метод сохранения данных в бд
        """
        for deal in self.deals:
            customer, _ = Customer.objects.get_or_create(
                username=deal['customer'],
            )
            gem, _ = Gem.objects.get_or_create(
                name=deal['item'],
            )
            deal['customer'] = customer.id
            deal['item'] = gem.id

        serializer = DealCreateSerializer(
            data=self.deals,
            many=True
        )
        serializer.is_valid()
        serializer.save()
