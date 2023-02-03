"""
Переопределите параметр с помощью indirect
Добавить параметры в фикстуру сторон браузера и запускать тесты в зависимости от сторон
"""

import pytest
from selene.support.shared import browser
from model.pages.github_page import open_page, \
    check_header_sign_in, \
    click_button_sign_in, \
    click_button_hamburger


@pytest.fixture(params=[(1920, 1080), (900, 940)])
def brow_config(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize('brow_config', [(1920, 1080)], indirect=True)
def test_github_desktop(brow_config):
    open_page()
    click_button_sign_in()
    check_header_sign_in()
    browser.close()


@pytest.mark.parametrize('brow_config', [(900, 940)], indirect=True)
def test_github_mobile(brow_config):
    open_page()
    click_button_hamburger()
    click_button_sign_in()
    check_header_sign_in()
