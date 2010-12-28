# -*- coding: utf-8 -*-
from core.tests import FunctionalCoreTestCase
from nose.tools import assert_true, assert_equals
from core.models import Conference

class FunctionalConferenceViewsSpec(FunctionalCoreTestCase):

    def test_new_conference_url_with_text(self):
        "New conference url (/conferences/new) should contain the text \"New conference\""
        response = self.client.get('/conferences/new')
        assert_true('New conference' in response.content)

    def should_save_a_conference_by_posting_data_to_new_conference_url(self):
        title = u'Python Brasil'
        response = self.client.post('/conferences/new', data={ u'title' : title, u'description' : u'Conferência brasileira de Python' })
        conference = Conference.objects.filter(title=title).all()[0]
        assert_equals(conference.title, title)
