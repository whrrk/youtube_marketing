import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Function.UploadAccountFile import get_file_path

def read_csv(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    # email과 password의 리스트 반환
    return df['email'].tolist(), df['password'].tolist()

def login_in_new_tab(driver,email, password, url):
    # 새로운 탭 열기
    driver.execute_script("window.open('');")
    
    # 새로 열린 탭으로 전환
    driver.switch_to.window(driver.window_handles[-1])
    
    # 로그인 페이지로 이동
    driver.get(url)
    
    # 로그인 폼 요소 찾기
    email_input = driver.find_element(By.NAME, "email")  # 이메일 입력 필드
    password_input = driver.find_element(By.NAME, "password")  # 비밀번호 입력 필드
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # 로그인 버튼
    
    # 이메일과 비밀번호 입력
    email_input.send_keys(email)
    password_input.send_keys(password)
    
    # 로그인 버튼 클릭
    login_button.click()
    
    time.sleep(5)

def login_multiple_accounts_in_tabs(csv_file_path, login_url):
    # CSV 파일에서 이메일과 비밀번호 리스트 가져오기
    emails, passwords = read_csv(csv_file_path)

    # 크롬 드라이버 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 각각의 계정에 대해 새로운 탭을 열고 로그인
    for email, password in zip(emails, passwords):
        print(f"로그인 시도: {email}")
        login_in_new_tab(driver, email, password, login_url)
        time.sleep(5)  # 탭 간의 지연 시간 (필요에 따라 조절 가능)
    
    # 모든 탭을 유지한 상태로 브라우저를 열어둠
    print("모든 계정 로그인 완료.")
    time.sleep(10)


if __name__ == "__LoginModel__":
    csv_file_path = get_file_path  # CSV 파일 경로 지정
    login_url = "https://accounts.google.com/"  # 로그인하려는 사이트의 로그인 페이지 URL

    login_multiple_accounts_in_tabs(csv_file_path, login_url)