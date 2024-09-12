from tkinter import filedialog
from tkinter import messagebox

def upload_file():
    # 파일 다이얼로그로 파일 선택
    file_path = filedialog.askopenfilename(
        title="텍스트 파일을 선택하세요",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    
    # 파일이 선택되었을 경우
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()  # 파일 내용 읽기
                return content
        except Exception as e:
            messagebox.showerror("Error", f"파일을 읽는 중 오류가 발생했습니다: {str(e)}")
    else:
        messagebox.showwarning("Warning", "파일을 선택하지 않았습니다.")