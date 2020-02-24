# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/

from selenium.common.exceptions import NoSuchElementException
import time

def test_guest_should_see_add_to_basket_button(browser):
    
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    
    browser.get(link)
    time.sleep(30)
    
    button = None
    
    try:
        button = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    except NoSuchElementException:
        pass
    
    assert button, '"Add to basket" button not founded'
