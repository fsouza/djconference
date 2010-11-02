from core.tests import FunctionalCoreTestCase
from nose.tools import assert_true

class FunctionalConferenceViewsSpec(FunctionalCoreTestCase):

    def test_something(self):
        response = self.client.get('/conferences/new')
        assert_true('New conference' in response.content)
