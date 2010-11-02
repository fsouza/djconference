from lettuce import step, world
from lettuce.django import django_url

@step(u'that I am on the new conference page')
def given_that_i_am_on_the_new_conference_page(step):
    url = django_url('/conferences/new')
    world.browser.get(url)

@step(u'I fill the conference "(.*)" with "(.*)"')
def when_i_fill_the_conference_field_with_value(step, field_name, value):
    field = world.browser.find_element_by_name(field_name)
    field.send_keys(value)

@step(u'I click on "(.*)" button')
def and_i_click_on_button(step, button_label):
    button = world.browser.find_element_by_xpath('//input[@type="submit" and @value="%s"]' % button_label)
    button.click()

@step(u'the conference "(.*)" should be in the database')
def then_the_conference_group1_should_be_in_the_database(step, group1):
    assert False, 'This step must be implemented'

@step(u'I should be redirected to the conferences list page')
def and_i_should_be_redirected_to_the_conferences_list_page(step):
    assert False, 'This step must be implemented'

@step(u'the conference "(.*)" should appear in the list')
def and_the_conference_group1_should_appear_in_the_list(step, group1):
    assert False, 'This step must be implemented'

