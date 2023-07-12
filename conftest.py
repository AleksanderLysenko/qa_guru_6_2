import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def browser_size():
    browser.config.window_width = 960
    browser.config.window_height = 540
