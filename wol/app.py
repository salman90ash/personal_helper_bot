from actions import create_webdriver, get_page_source, form_processing, close_webdriver
from settings import URL

url = URL
chrome = create_webdriver()
get_page_source(webdriver=chrome, url=url)
form_processing(webdriver=chrome)
close_webdriver(webdriver=chrome)
print('done!')