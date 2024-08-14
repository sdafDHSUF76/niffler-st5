from typing import TYPE_CHECKING

import pytest

from niffler_e_2_e_tests_python.presentation.authorization.login_page import LoginPage

if TYPE_CHECKING:
    from playwright.sync_api import Page


@pytest.fixture(scope='class')
def login_page(driver: 'Page') -> LoginPage:
    """Получаем страницу Login со всей логикой ее."""
    return LoginPage(driver)
