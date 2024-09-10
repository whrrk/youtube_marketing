from selenium.webdriver.common.by import By
from Function.ProxyAndDriverSetting import driver
import time

# 구글 계정 정보
email = "your_email@gmail.com"
password = "your_password"

# 구글 로그인 페이지로 이동
driver.get("https://accounts.google.com/signin")

# 이메일 입력 및 다음 버튼 클릭
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(email)
driver.find_element(By.ID, "identifierNext").click()
time.sleep(3)

# 비밀번호 입력 및 다음 버튼 클릭
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
driver.find_element(By.ID, "passwordNext").click()

# 로그인 대기
time.sleep(5)