from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from contextlib import contextmanager

@contextmanager
def get_driver():
    # 크롬 일반 옵션
    options = Options()
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach",True)
    options.add_experimental_option("excludeSwitches",["enable-logging"])

    # 크롬 프록시 설정
    # 사용할 프록시 IP:PORT
    # proxy = "123.45.67.89:8080"  
    # options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # 크롬 드라이버 설정
    try:
        yield driver
    
    finally:
        print("complete")