import mocker
from core.tests import RequestFactory, CoreTestCase
from core.views import new_conference, list_conferences
from core.forms import ConferenceForm
from django.http import HttpResponse

class TestConferenceViews(CoreTestCase):

    def setup(self):
        super(TestConferenceViews, self).setup()
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

    def it_should_list_conferences_on_list_conferences_view_rendering_conferences_html_template(self):
        request = self.request_factory.get('/conferences')

        conferences = ['conference 1', 'conference 2', 'conference 3']

        mock_conference_all = self.mocker.replace('core.models.Conference.objects.all')
        mock_conference_all()
        self.mocker.result(conferences)

        response = self.mocker.mock(HttpResponse)
        mock_render_to_response = self.mocker.replace('django.shortcuts.render_to_response')
        mock_render_to_response('conferences.html', { 'conferences' : conferences }, mocker.KWARGS)
        self.mocker.result(response)

        self.mocker.replay()
        list_conferences(request)
        self.mocker.verify()
