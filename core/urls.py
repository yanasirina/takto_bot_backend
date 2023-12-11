from rest_framework import routers

import core.views.user


app_name = 'core'

urlpatterns = []

router = routers.DefaultRouter()
router.register('users', core.views.user.UserViewSet, basename='users')
router.register('students', core.views.user.UserViewSet, basename='students')


urlpatterns += router.urls
