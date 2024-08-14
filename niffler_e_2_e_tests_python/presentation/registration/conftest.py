from typing import TYPE_CHECKING

import pytest

from niffler_e_2_e_tests_python.configs import AUTH_URL
from niffler_e_2_e_tests_python.presentation.registration.register_page import RegisterPage

if TYPE_CHECKING:
    from playwright.sync_api import Page

    from niffler_e_2_e_tests_python.fixtures.database import DB


@pytest.fixture(scope='class')
def registration_page(driver: 'Page') -> RegisterPage:
    """Получаем страницу Main со всей логикой ее."""
    return RegisterPage(driver)


@pytest.fixture
def goto_registration_url(registration_page: RegisterPage) -> None:
    """Получаем страницу Main со всей логикой ее."""

    if f'{AUTH_URL}{registration_page.path}' != registration_page.driver.url:
        registration_page.goto_url(f'{AUTH_URL}{registration_page.path}')


@pytest.fixture
def clear_extra_users(db_niffler_auth: 'DB'):
    yield
    db_niffler_auth.execute(
        'delete from authority a where user_id in (select id from "user" where username != \'qwe\')'
    )
    db_niffler_auth.execute('delete from "user" where username != \'qwe\'')
