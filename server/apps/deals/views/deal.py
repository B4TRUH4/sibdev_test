from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers import CustomerSerializer
from ..models import Customer
from ..services import DealFileHandler
from ..utils import clear_database
from ..constants import CacheConstant


class DealsUploadView(views.APIView):
    """
    APIView аналитики по сделкам
    """
    def post(self, request: Request):
        file = request.data['file']
        clear_database()
        errors = DealFileHandler(file=file).import_data_from_csv_file()
        if not errors:
            cache.clear()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                {'desc': errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    @method_decorator(cache_page(CacheConstant.CACHE_TIME))
    def get(self, request: Request):
        serializer = CustomerSerializer(
            Customer.objects.all()
            .annotate_with_spent_money()
            .get_top_customers()
            .annotate_with_top_gems(), many=True
        )
        return Response(
            {'response': serializer.data},
            status=status.HTTP_200_OK
        )
