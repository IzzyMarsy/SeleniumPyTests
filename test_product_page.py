import pytest

from pages.product_page import ProductPage


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.execute_shopping_workflow()

