import mocker
from core.tests import RequestFactory, CoreTestCase
from core.views import new_conference
from core.forms import ConferenceForm
from django.http import HttpResponse

class TestConferenceViews(CoreTestCase):

    def setUp(self):
        super(TestConferenceViews, self).setUp()
        self.request_factory = RequestFactory()

    def it_should_show_conference_form_on_new_conference_view_rendering_new_conference_html_template(self):
        request = self.request_factory.get('/conferences/new')
        form = self.mocker.mock(ConferenceForm)

        mock_form = self.mocker.replace('core.forms.ConferenceForm')
        mock_form()
        self.mocker.result(form)

        response = self.mocker.mock(HttpResponse)
        mock_render_to_response = self.mocker.replace('django.shortcuts.render_to_response')
        mock_render_to_response('new_conference.html', { 'form' : form }, mocker.KWARGS)
        self.mocker.result(response)

        self.mocker.replay()
        new_conference(request)
        self.mocker.verify()
