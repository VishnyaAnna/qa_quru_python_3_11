import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_config_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def browser_config_mobile():
    browser.config.window_width = 900
    browser.config.window_height = 940