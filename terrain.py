from lettuce import before, after, world
from selenium import get_driver, FIREFOX
from django.conf import settings

@before.all
def setup_selenium():
    world.browser = get_driver(FIREFOX, profile='selenium')
    settings.DEBUG = True

@after.all
def teardown_selenium(total):
    world.browser.quit()
