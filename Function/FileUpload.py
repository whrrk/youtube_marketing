import tkinter as tk
from tkinter import filedialog

def open_file():
    # Tkinter 윈도우를 생성하지 않고 초기화.
    root = tk.Tk()
    root.withdraw()  # Tkinter 윈도우를 숨김.

    # 파일 대화 상자를 열어 사용자가 파일을 선택.
    file_path = filedialog.askopenfilename(
        title="파일 선택",
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )

    if file_path:  # 사용자가 파일을 선택했을 경우
        try:
            # 선택한 파일을 열고 내용을 읽음.
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

        except Exception as e:
            print(f"파일을 읽는 중 오류가 발생했습니다: {e}")


# 함수 호출 (파일 업로드 버튼 누르는 이벤트 발생 시)
content = open_file()

# # 파일 선택 및 업로드 함수
# def upload_file():
#     file_path = filedialog.askopenfilename()  # 파일 선택 창 열기
#     if file_path:
#         # 여기서 파일을 처리하거나 업로드.
#         messagebox.showinfo("파일 선택됨", f"선택된 파일: {file_path}")
#     else:
#         messagebox.showwarning("파일 선택 취소", "파일이 선택되지 않았습니다.")



# # 업로드 버튼
# upload_btn = tk.Button(root, text="파일 업로드", command=upload_file)
# upload_btn.pack(pady=50)

# # 메인 루프 실행
# root.mainloop()