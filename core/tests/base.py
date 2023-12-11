from django.contrib.auth.models import Permission
from django.test import TestCase

from core import models


class BaseRestTestCase(TestCase):
    username = 'test'
    password = 'testtest'
    permission = None
    any_permissions = None

    def get_permission(self):
        return self.permission

    def get_any_permissions(self):
        return self.any_permissions

    def generate_data(self):
        pass

    def user_config(self):
        perms = []
        if self.get_permission():
            perms.append(self.get_permission().split('.'))
        elif self.get_any_permissions():
            perms.extend([perm.split('.') for perm in self.get_any_permissions()])

        for app_label, codename in perms:
            self.user.user_permissions.add(
                Permission.objects.get(content_type__app_label=app_label, codename=codename)
            )

    def create_user(self):
        self.user = models.DjangoUser.objects.create(
            username=self.username,
            password=self.password,
        )
        self.user_config()

    def setUp(self):
        self.create_user()
        self.generate_data()
        self.client.force_login(self.user)
