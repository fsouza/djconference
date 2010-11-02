from core.tests import FunctionalCoreTestCase
from nose.tools import assert_true

class FunctionalConferenceViewsSpec(FunctionalCoreTestCase):

    def test_new_conference_url_with_text(self):
        "New conference url (/conferences/new) should contain the text \"New conference\""
        response = self.client.get('/conferences/new')
        assert_true('New conference' in response.content)
