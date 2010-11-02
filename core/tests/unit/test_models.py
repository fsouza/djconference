import mocker
from core.models import Conference
from django.db import IntegrityError
from nose.tools import raises

class TestModels(mocker.MockerTestCase):

    @raises(IntegrityError)
    def should_not_add_a_conference_without_title(self):
        c = Conference()
        c.title = None
        c.description = 'My description'
        c.save()

    @raises(IntegrityError)
    def should_not_add_a_conference_without_description(self):
        c = Conference()
        c.title = 'My title'
        c.description = None
        c.save()

