from settings import EXECUTABLE_PATH, PROXY_OPTIONS, LOGIN, PASSWORD
import time
from selenium import webdriver
from seleniumwire import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def create_webdriver(proxy: bool = False, background_mode: bool = True) -> webdriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    if background_mode:
        chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    if proxy:
        seleniumwire_options = {
            'proxy': {
                'http': f'http://{PROXY_OPTIONS}',
                'https': f'https://{PROXY_OPTIONS}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }
        chrome = webdriver.Chrome(executable_path=r"/home/student/chromedriver",
                                  service=Service(ChromeDriverManager().install()),
                                  options=chrome_options,
                                  seleniumwire_options=seleniumwire_options)
    else:
        chrome = webdriver.Chrome(executable_path=EXECUTABLE_PATH,
                                  service=Service(ChromeDriverManager().install()),
                                  options=chrome_options)
    stealth(
        driver=chrome,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)Chrome/109.0.0.0 Safari/537.36",
        languages=["ru", "en"],
        platform="Win32",
        webgl_vendor="Google Inc. (NVIDIA)",
        renderer="ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)",
        fix_hairline=True,
        run_on_insecure_origins=False
    )
    return chrome


def get_page_source(webdriver: webdriver, url: str):
    chrome = webdriver
    chrome.get(url)


def form_processing(webdriver: webdriver):
    chrome: webdriver = webdriver
    login = chrome.find_element(by=By.ID, value='login_username')
    login.send_keys(LOGIN)
    password = chrome.find_element(by=By.NAME, value='login_passwd')
    password.send_keys(PASSWORD)
    btn_log_in = chrome.find_element(by=By.CLASS_NAME, value="button")
    btn_log_in.click()
    time.sleep(8)
    mac_address = chrome.find_element(
        by=By.XPATH,
        value=r"/html/body/form[1]/table/tbody/tr/td[3]/div/table/tbody/tr/"
              r"td/table/tbody/tr/td/div[6]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div[2]"
    )
    mac_address.click()
    time.sleep(1)
    btn_wake_up = chrome.find_element(by=By.ID, value="cmdBtn")
    btn_wake_up.click()
    time.sleep(2)
    btn_exit = chrome.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/a[1]/div/span"
    )
    btn_exit.click()
    time.sleep(2)

    alert = chrome.switch_to.alert
    alert.accept()
    time.sleep(2)


def close_webdriver(webdriver: webdriver):
    webdriver.close()
    webdriver.quit()
