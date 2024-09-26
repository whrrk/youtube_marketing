import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Function.ProxyAndDriverSetting import get_driver
from tkinter import messagebox
from Model.MainModel import traffic_run

upload_account_file_path = None
upload_proxy_file_path = None

def login_multiple_accounts_in_browser(csv_file_path,csv_proxy_file_path, login_url):
    # CSV 파일에서 이메일과 비밀번호 리스트 가져오기
    emails, passwords = read_csv(csv_file_path)

    # 각각의 계정에 대해 새로운 탭을 열고 로그인
    for email, password in zip(emails, passwords):
        print(f"로그인 시도: {email}")
        login_in_new_browser(email, password, login_url)
        time.sleep(5)  # 탭 간의 지연 시간 (필요에 따라 조절 가능)
    
    # 모든 탭을 유지한 상태로 브라우저를 열어둠
    print("모든 계정 로그인 완료.")
    time.sleep(10)

def read_csv(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    # email과 password의 리스트 반환
    return df['email'].tolist(), df['password'].tolist()

def login_in_new_browser(email, password, url):
    # 새로운 탭 열기
    # driver.execute_script("window.open('');")
    
    # 새로 열린 탭으로 전환
    # driver.switch_to.window(driver.window_handles[-1])
    
    # 로그인 페이지로 이동
    with get_driver() as driver:
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

    traffic_run(driver)

def run():
    csv_account_file_path = upload_account_file_path  # CSV 파일 경로 지정
    csv_proxy_file_path = upload_proxy_file_path

    if csv_account_file_path and csv_proxy_file_path:
        login_url = "https://accounts.google.com/"  # 로그인하려는 사이트의 로그인 페이지 URL

        login_multiple_accounts_in_browser(csv_account_file_path,csv_proxy_file_path,login_url)
    else:
        messagebox.showinfo("알림", "CSV 파일 업로드 후 실행 해 주세요.")
