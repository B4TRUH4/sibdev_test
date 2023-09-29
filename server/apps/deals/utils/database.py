from ..models import Deal, Customer, Gem


def clear_database():
    """
    Функция очистки базы данных
    """
    Deal.objects.all().delete()
    Customer.objects.all().delete()
    Gem.objects.all().delete()
