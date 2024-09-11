#  setting 관련 ini 파일 내용 파싱하기.
#  실행주기(탭 켜고 로그인 대기시간)
#  로그인 후 유튜브 링크 접속까지 대기시간
#  프록시 적용 및 최대 탭 갯수 설정
#  머무는 시간 설정

import configparser

# ConfigParser 객체 생성
config = configparser.ConfigParser()

# ini 파일 읽기
config.read('setting.ini')

# 섹션과 옵션에 접근하는 방법
app_name = config['DEFAULT']['AppName']
version = config['DEFAULT']['Version']
# 각 로그인 대기시간
login_wait = config['DEFAULT']['LoginWaitTime']
# 각 유튜브 접속 대기시간
youtube_wait = config['DEFAULT']['YoutubeWaitTime']
# 유지시간
duration = config['DEFAULT']['Duration']

options = [app_name,
           version,
           login_wait,
           youtube_wait,
           duration]


