from typing import TYPE_CHECKING

import pytest
from playwright.sync_api import expect

from niffler_e_2_e_tests_python.configs import TEST_PASSWORD, TEST_USER
from niffler_e_2_e_tests_python.presentation.authorization.enums import ErrorAuthorization
from niffler_e_2_e_tests_python.presentation.authorization.main.conftest import main_page  # noqa F401

if TYPE_CHECKING:
    from niffler_e_2_e_tests_python.presentation.authorization.login_page import LoginPage
    from niffler_e_2_e_tests_python.presentation.authorization.main.main_page import MainPage


class TestAuthorization:

    @pytest.mark.usefixtures('go_login_page', 'logout', 'clear_storage')
    def test_authorization(self, login_page: 'LoginPage', main_page: 'MainPage'):
        login_page.authorization(TEST_USER, TEST_PASSWORD)
        expect(main_page.driver.locator(main_page.header)).to_have_text(main_page.text_header)

    @pytest.mark.usefixtures('go_login_page')
    @pytest.mark.parametrize('login', ['asdf', 'qwer', 'we', ' ', ' ', '\32%$^&*('])
    def test_authorization_with_invalid_login(self, login: str, login_page: 'LoginPage'):
        login_page.authorization(login, TEST_PASSWORD)
        expect(login_page.driver.locator(login_page.text_error)).to_have_text(
            ErrorAuthorization.INVALID_USER_CREDENTIALS,
        )
