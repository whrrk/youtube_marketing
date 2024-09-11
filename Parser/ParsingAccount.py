# 구글계정(ID, PW) 입력 ini파일 내용 파싱하기.

with open('example.txt', 'r') as file:
    for line in file:
        data = line.strip().split(',')  # 콤마(,)로 분리
        name = data[0]
        age = data[1]
        country = data[2]
        print(f"Name: {name}, Age: {age}, Country: {country}")