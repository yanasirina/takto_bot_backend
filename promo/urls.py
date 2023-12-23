from rest_framework import routers

import promo.views.promocode


app_name = 'promo'

urlpatterns = []
router = routers.DefaultRouter()

router.register('promocodes', promo.views.promocode.PromoCodeViewSet, basename='promocodes')

urlpatterns += router.urls
