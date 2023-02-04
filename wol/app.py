from wol.actions import create_webdriver, get_page_source, form_processing, close_webdriver
from wol.settings import URL


def run_app():
    url = URL
    chrome = create_webdriver()
    get_page_source(webdriver=chrome, url=url)
    form_processing(webdriver=chrome)
    close_webdriver(webdriver=chrome)
    print("Salman's computer is on!")


if __name__ == '__app__':
    pass
