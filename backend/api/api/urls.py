from django.contrib import admin
from django.urls import path
from .views import get_trove_stake

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trove-stake/', get_trove_stake, name='trove-stake'),
]
