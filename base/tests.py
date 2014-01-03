"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# django
from django.test import TestCase

# models
from users.models import User
from cms.models import Interview
from cms.models import Tag

# standard library
import random
import string


class BaseTestCase(TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()

        self.user = self.create_user()

    def create_interview(self, **kwargs):
        return Interview.objects.create(**kwargs)

    def create_tag(self):
        return Tag.objects.create(
            title=self.random_string(),
            link="http://{}.com".format(self.random_string())
        )

    def create_user(self, password=None, **kwargs):
        if kwargs.get('first_name') is None:
            kwargs['first_name'] = self.random_string(length=6)

        if kwargs.get('last_name') is None:
            kwargs['last_name'] = self.random_string(length=6)

        if kwargs.get('email') is None:
            kwargs['email'] = "%s@gmail.com" % self.random_string(length=6)

        if kwargs.get('is_active') is None:
            kwargs['is_active'] = True

        user = User.objects.create(**kwargs)

        if password is not None:
            user.set_password(password)
            user.save()

        return user

    def login(self, user, password):
        uri = "%slogin/" % self.user_resource_uri
        data = {
            "email": user.email,
            "password": password,
        }

        response = self.client.post(uri, data=data)
        self.assertEqual(response.status_code, 200)

    def random_string(self, length=6):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for x in range(length))
