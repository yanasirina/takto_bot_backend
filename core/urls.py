from rest_framework import routers

import core.views.user
import core.views.course


app_name = 'core'

urlpatterns = []

router = routers.DefaultRouter()
router.register('users', core.views.user.UserViewSet, basename='users')
router.register('courses', core.views.course.CourseViewSet, basename='courses')

urlpatterns += router.urls
