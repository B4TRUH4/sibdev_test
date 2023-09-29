from django.urls import path
from .views import DealsUploadView

urlpatterns = [
    path('', DealsUploadView.as_view(), name='deals'),
]
