from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Chrome 웹드라이버 경로 설정 (다운로드 받은 chromedriver의 경로로 설정)
chrome_driver_path = "path/to/chromedriver"

# 프록시 설정 (HTTP 프록시 예시)
proxy = "123.45.67.89:8080"  # 사용할 프록시 IP:PORT

# 프록시 설정을 적용하는 방법
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy}')

# Chrome 드라이버 설정
service = Service(executable_path=chrome_driver_path,options=chrome_options)
driver = webdriver.Chrome(service=service)

