import mocker
from core.models import Conference
from django.db import IntegrityError
from nose.tools import raises

class TestConferenceModels(mocker.MockerTestCase):

    def _get_conference(self, title = None, description = None):
        conference = Conference(title = title, description = description)
        return conference

    @raises(IntegrityError)
    def should_not_add_a_conference_without_title(self):
        c = self._get_conference(title=None, description='My description')
        c.save()

    @raises(IntegrityError)
    def should_not_add_a_conference_without_description(self):
        c = self._get_conference(title='My title', description=None)
        c.save()

    def should_add_a_conference_with_title_and_description(self):
        c = self._get_conference(title='My title', description='My description')
        c.save()
