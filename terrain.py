from lettuce import before, after, world
from selenium.firefox.webdriver import WebDriver

@before.all
def setup_selenium():
    world.browser = WebDriver(profile='selenium')

@after.all
def teardown_selenium(total):
    world.browser.quit()
