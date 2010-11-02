from lettuce import before, after, world
from selenium import get_driver, FIREFOX

@before.all
def setup_selenium():
    world.browser = get_driver(FIREFOX, profile='selenium')

@after.all
def teardown_selenium(total):
    world.browser.quit()
