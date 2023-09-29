from django.urls import path, include

urlpatterns = [
    path('deals/', include('apps.deals.urls')),
]