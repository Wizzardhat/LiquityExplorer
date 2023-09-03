from django.contrib import admin
from django.urls import path
from .views import (get_trove_stake,
                    get_historical_number_of_troves,
                    get_staked_lqty_token_amount,
                    get_best_troves,
                    get_worst_troves,
                    get_historical_number_of_eth_lusd,
                    get_redemption_events,
                    get_trove_liquidation_events,
                    )

urlpatterns = [
     path('admin/', admin.site.urls),
     path('trove-stake/', get_trove_stake, name='trove-stake'),
     path('get_historical_number_of_troves/',
          get_historical_number_of_troves, name='historical-number-of-troves'),
     path('get_staked_lqty_token_amount/',
          get_staked_lqty_token_amount, name='staked-lqty-token-amount'),
     path('get-best-troves/', get_best_troves, name='get-best-troves'),
     path('get-worst-troves/', get_worst_troves, name='get-best-troves'),
     path('get-historical-number-of-eth-lusd/', get_historical_number_of_eth_lusd, name='get-historical-number-of-eth-lusd'),
     path('get-redemptions-events/', get_redemption_events, name='get-redemption-events'),
     path('get-trove-liquidation-events/', get_trove_liquidation_events, name='get-trove-liquidation-events')
]
