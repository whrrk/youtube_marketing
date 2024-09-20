import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

upload_file_path = None

def login_multiple_accounts_in_tabs(csv_file_path, login_url):
    # CSV 파일에서 이메일과 비밀번호 리스트 가져오기
    emails, passwords = read_csv(csv_file_path)

    options = Options()
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach",True)
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    # 크롬 드라이버 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 각각의 계정에 대해 새로운 탭을 열고 로그인
    for email, password in zip(emails, passwords):
        print(f"로그인 시도: {email}")
        login_in_new_tab(driver, email, password, login_url)
        time.sleep(5)  # 탭 간의 지연 시간 (필요에 따라 조절 가능)
    
    # 모든 탭을 유지한 상태로 브라우저를 열어둠
    print("모든 계정 로그인 완료.")
    time.sleep(10)

def read_csv(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    # email과 password의 리스트 반환
    return df['email'].tolist(), df['password'].tolist()

def login_in_new_tab(driver,email, password, url):
    # 새로운 탭 열기
    # driver.execute_script("window.open('');")
    
    # 새로 열린 탭으로 전환
    # driver.switch_to.window(driver.window_handles[-1])
    
    # 로그인 페이지로 이동
    driver.get(url)
    
    # 이메일 입력
    email_input = driver.find_element(By.NAME, 'identifier')
    email_input.send_keys(email)  # 자신의 이메일 입력
    email_input.send_keys(Keys.RETURN)

    # 잠시 대기
    time.sleep(5)
    # 비밀번호 입력
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))  # ID가 "element_id"인 요소가 나타날 때까지 대기
    )
    password_input.send_keys(password)  # 자신의 비밀번호 입력
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(5)

def run():
    csv_file_path = upload_file_path  # CSV 파일 경로 지정

    login_url = "https://accounts.google.com/"  # 로그인하려는 사이트의 로그인 페이지 URL

    login_multiple_accounts_in_tabs(csv_file_path, login_url)