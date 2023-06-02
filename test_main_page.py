import pytest

from page.main_page import MainPage


class TestLoginPage:
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/"])
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/"])
    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()