"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот) с помощью марки скип
"""
import pytest
from selene.support.shared import browser
from model.pages.github_page import open_page,\
    click_button_sign_in,\
    click_button_hamburger,\
    check_header_sign_in


@pytest.mark.parametrize("width, height", [pytest.param(1900, 1080), pytest.param(900, 940)])
def test_github_desktop(width, height):
    if width == 900:
        pytest.skip("Размер окна под мобильную версию!")
    browser.config.window_width = width
    browser.config.window_height = height
    open_page()
    click_button_sign_in()
    check_header_sign_in()


@pytest.mark.parametrize("width, height", [pytest.param(1900, 1080), pytest.param(900, 940)])
def test_github_mobile(width, height):
    if width == 1900:
        pytest.skip("Размер окна под десктопную версию!")
    browser.config.window_width = width
    browser.config.window_height = height
    open_page()
    click_button_hamburger()
    click_button_sign_in()
    check_header_sign_in()