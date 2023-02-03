import pytest
from selene.support.shared import browser


# Сделайте разные фикстуры для каждого теста
def test_github_desktop(setup_desktop):
    browser.element('[name=q]').press_enter()


def test_github_mobile(setup_mobile):
    browser.element('[name=q]').press_enter()


# Переопределите параметр с помощью indirect
@pytest.mark.parametrize("window_size", ["990*960"], indirect=True)
def test_github_mobile_indirect(window_size):
    browser.element('[name=q]').click()


@pytest.mark.parametrize("window_size", ["1920*1080"], indirect=True)
def test_github_desktop_indirect(window_size):
    browser.element('[name=q]').click()


# Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
@pytest.mark.parametrize("window_width,window_height",
                         [pytest.param(1920, 1080),
                          pytest.param(990, 960)
                          ])
def test_github_desktop_reason(browser_chrome, window_width, window_height):
    if window_width == 990:
        pytest.skip(reason='Пропускаем мобильную версию в тесте')
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.element('[name=q]').click()


@pytest.mark.parametrize("window_width,window_height",
                         [pytest.param(1920, 1080, id="desktop version"),
                          pytest.param(990, 960, id="mobile_version")
                          ])
def test_github_mobile_reason(browser_chrome, window_width, window_height):
    if window_width == 1920:
        pytest.skip(reason='Пропускаем десктопную версию в тесте')
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.element('[name=q]').click()

