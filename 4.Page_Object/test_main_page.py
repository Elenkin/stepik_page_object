""" PyTest --tb=line, выводит только одну строку из лога каждого упавшего теста """


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
