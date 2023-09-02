from django.contrib import admin
from django.urls import path
from .views import TroveStakeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('trove-stake/', TroveStakeView.as_view(), name='trove-stake'),
]
