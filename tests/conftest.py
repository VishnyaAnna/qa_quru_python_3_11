import pytest
from selene.support.shared import browser


@pytest.fixture
def setup_desktop(browser_chrome):
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()


@pytest.fixture
def setup_mobile(browser_chrome):
    browser.config.window_width = 960
    browser.config.window_height = 990
    yield
    browser.quit()


@pytest.fixture()
def browser_chrome():
    browser.open('https://github.com')


@pytest.fixture(params=["1920*1080", "990*960"])
def window_size(browser_chrome, request):
    if request.param == "1920*1080":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == "990*960":
        browser.config.window_width = 990
        browser.config.window_height = 960
