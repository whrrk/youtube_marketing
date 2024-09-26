import time
from selenium.webdriver.common.by import By
from Function.ProxyAndDriverSetting import driver

# 유튜브 영상 URL로 이동
time.sleep(5)  # 페이지 로딩 대기

# (옵션) 영상이 자동으로 재생되지 않으면 플레이 버튼 클릭
try:
    play_button = driver.find_element(By.CLASS_NAME, "ytp-large-play-button")
    play_button.click()
except:
    pass  # 이미 재생 중일 경우 예외 처리

time.sleep(3)

# 좋아요
try:
    like_button = driver.find_element(By.XPATH, '//*[@aria-label="좋아요"]')
    like_button.click()
except:
    print("좋아요 버튼을 찾을 수 없습니다.")

time.sleep(3)

# 구독
try:
    subscribe_button = driver.find_element(By.XPATH, '//*[@aria-label="구독"]')
    subscribe_button.click()
except:
    print("구독 버튼을 찾을 수 없습니다.")

# 작업 완료 후 대기 또는 브라우저 종료 코드 삽입하기
time.sleep(5)