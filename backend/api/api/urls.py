from django.contrib import admin
from django.urls import path
from .views import get_trove_stake, get_historical_number_of_troves

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trove-stake/', get_trove_stake, name='trove-stake'),
    path('get_historical_number_of_troves/',
         get_historical_number_of_troves, name='historical-number-of-troves')
]
