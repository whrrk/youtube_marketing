import configparser
import chardet

#  setting 관련 ini 파일 내용 파싱하기.
#  실행주기(탭 켜고 로그인 대기시간)
#  로그인 후 유튜브 링크 접속까지 대기시간
#  프록시 적용 및 최대 탭 갯수 설정
#  머무는 시간 설정

# ini 파일 읽기
with open('setting.ini','rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# ConfigParser 객체 생성
config = configparser.ConfigParser()
with open('setting.ini', 'r', encoding=encoding) as file:
    config.read_file(file)

# 섹션별 데이터 출력
for section in config.sections():
    print(f"[{section}]")
    for key,value in config.items(section):
        print(f"{key} = {value}")
# 섹션과 옵션에 접근하는 방법
app_name = config['DEFAULT']['AppName']
version = config['DEFAULT']['Version']
# 각 로그인 대기시간
login_wait = config['DEFAULT']['LoginWaitTime']
# 각 유튜브 접속 대기시간
youtube_wait = config['DEFAULT']['YoutubeWaitTime']
# 유지시간
duration = config['DEFAULT']['Duration']
# 반복횟수
repeat_count = config['DEFAULT']['Repeat']
# 유튜브 url
youtube_url = config['DEFAULT']["YoutubeUrl"]
settings = {'app_name': app_name,
            'version': version,
            'login_wait':login_wait,
            'youtube_wait':youtube_wait,
            'duration':duration,
            'repeat_count':repeat_count,
            'youtube_url':youtube_url}
