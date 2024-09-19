# 구글계정(ID, PW) 입력 ini파일 내용 파싱하기.

from tkinter import messagebox
import csv

account_data = []
def ParsingAccount(file_path):
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    account_data.append(row)  # 각 행을 배열에 저장
        except Exception as e:
            messagebox.showerror("Error", f"파일을 읽는 중 오류가 발생했습니다: {str(e)}")
    else:
        messagebox.showwarning("Warning", "파일을 선택하지 않았습니다.")

    return account_data

