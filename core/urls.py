from rest_framework import routers
from django.urls import path

import core.views.user
import core.views.course
import core.views.student
import core.views.auth


app_name = 'core'

urlpatterns = [path('auth', core.views.auth.AuthTokenView.as_view(), name='auth-token'),
               ]

router = routers.DefaultRouter()
router.register('users', core.views.user.UserViewSet, basename='users')
router.register('courses', core.views.course.CourseViewSet, basename='courses')
router.register('students', core.views.student.StudentViewSet, basename='students')

urlpatterns += router.urls
